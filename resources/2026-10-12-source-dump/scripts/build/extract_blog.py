#!/usr/bin/env python3
"""Extract the visible article body of a blog post from a saved HTML file.

Usage: python3 -I extract_blog.py RAW_HTML_PATH

stdout: article body text (prose, headings-as-text, list items prefixed "- ",
        block quotes prefixed "> ", code blocks verbatim with indentation),
        followed by a section headed "LINKS IN ARTICLE BODY".
stderr: a manifest of everything dropped as page chrome or post-meta, so the
        caller can record exactly what was removed.

Standard library only (html.parser).
"""
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urljoin

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input",
        "link", "meta", "source", "track", "wbr"}
SKIP_TEXT = {"script", "style", "noscript", "template"}
CHROME_LABELS = ("head", "header", "aside", "footer", "nav", "script", "style")


def collapse(s):
    return re.sub(r"\s+", " ", s).strip()


class Extractor(HTMLParser):
    def __init__(self, base_url):
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.stack = []            # open non-void tags
        self.in_body = False       # inside <div id="blog">
        self.body_div_depth = 0
        self.suppress = []         # entries: ("h1", None) or ("div", depth)
        self.blocks = []
        self.buf = []
        self.pre = None            # list of raw strings while inside <pre>
        self.bq = 0
        self.li = 0
        self.cur_link = None
        self.links = []
        self.dropped = []          # (label, text)
        self.dropped_links = []    # (label, text, href)
        self.dropped_images = 0
        self.images = 0

    # ---- helpers -------------------------------------------------------
    def _label(self):
        for t in self.stack:
            if t in CHROME_LABELS:
                return t
        return "other"

    def _in_skip_text(self):
        return any(t in SKIP_TEXT for t in self.stack)

    def _flush(self):
        text = collapse("".join(self.buf))
        self.buf = []
        if not text:
            return
        if self.li:
            text = "- " + text
        if self.bq:
            text = "\n".join("> " + line for line in text.split("\n"))
        self.blocks.append(text)

    def _emit_pre(self):
        raw = "".join(self.pre or [])
        self.pre = None
        raw = raw.strip("\n")
        if not raw.strip():
            return
        if self.bq:
            raw = "\n".join("> " + line if line else ">" for line in raw.split("\n"))
        self.blocks.append(raw)

    # ---- parser callbacks ---------------------------------------------
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag in VOID:
            self._void(tag, a)
            return
        if not self.in_body:
            if tag == "div" and a.get("id") == "blog":
                self.in_body = True
                self.body_div_depth = 1
                self.stack.append(tag)
                return
            if tag == "a" and a.get("href"):
                self.dropped_links.append((self._label(), None, a["href"]))
            self.stack.append(tag)
            return

        # inside body
        if tag == "div":
            self.body_div_depth += 1
            if "date" in (a.get("class") or "").split():
                self._flush()
                self.suppress.append(("div", self.body_div_depth))
            elif not self.suppress:
                self._flush()
        elif tag == "h1":
            self._flush()
            self.suppress.append(("h1", None))
        elif tag == "pre":
            self._flush()
            self.pre = []
        elif tag in ("p", "ul", "ol", "h2", "h3", "h4", "h5", "h6", "figure", "table"):
            self._flush()
        elif tag == "blockquote":
            self._flush()
            self.bq += 1
        elif tag == "li":
            self._flush()
            self.li += 1
        elif tag == "a":
            if a.get("href"):
                self.cur_link = {"href": a["href"], "text": []}
        elif tag == "img":
            pass
        self.stack.append(tag)

    def _void(self, tag, a):
        if tag == "img":
            if self.in_body:
                self.images += 1
                alt = collapse(a.get("alt") or "")
                if alt and not self._suppressed():
                    self.buf.append(f"[image: {alt}]")
            else:
                self.dropped_images += 1
        elif tag == "br":
            if self.in_body and not self._suppressed():
                if self.pre is not None:
                    self.pre.append("\n")
                else:
                    self.buf.append(" ")
        elif tag == "hr":
            if self.in_body and not self._suppressed():
                self._flush()
                self.blocks.append("---")

    def _suppressed(self):
        return bool(self.suppress)

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)
        if tag not in VOID:
            self.handle_endtag(tag)

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if self.in_body:
            if tag == "div":
                if self.suppress and self.suppress[-1] == ("div", self.body_div_depth):
                    self.suppress.pop()
                else:
                    self._flush()
                self.body_div_depth -= 1
                if self.body_div_depth == 0:
                    self._flush()
                    self.in_body = False
            elif tag == "h1":
                if self.suppress and self.suppress[-1] == ("h1", None):
                    self.suppress.pop()
                self._flush()
            elif tag == "pre":
                if self.pre is not None:
                    self._emit_pre()
            elif tag in ("p", "ul", "ol", "h2", "h3", "h4", "h5", "h6", "figure", "table"):
                self._flush()
            elif tag == "blockquote":
                self._flush()
                self.bq -= 1
            elif tag == "li":
                self._flush()
                self.li -= 1
            elif tag == "a":
                if self.cur_link is not None:
                    text = collapse("".join(self.cur_link["text"]))
                    self.links.append((text, urljoin(self.base_url, self.cur_link["href"])))
                    self.cur_link = None
        # pop the most recent matching open tag
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i] == tag:
                del self.stack[i]
                break

    def handle_data(self, data):
        if not data:
            return
        if not self.in_body or self._in_skip_text():
            if data.strip():
                self.dropped.append((self._label() if not self.in_body else "script/style", data.strip()))
            return
        if self.suppress:
            if data.strip():
                self.dropped.append(("post title/date (h1, date line)", data.strip()))
            return
        if self.pre is not None:
            self.pre.append(data)
        else:
            self.buf.append(data)
        if self.cur_link is not None:
            self.cur_link["text"].append(data)

    def close(self):
        super().close()
        if self.in_body:
            self._flush()


def main():
    if len(sys.argv) != 2:
        sys.stderr.write("usage: extract_blog.py RAW_HTML_PATH\n")
        return 2
    base = "https://blog.cleancoder.com/uncle-bob/2014/05/08/SingleReponsibilityPrinciple.html"
    with open(sys.argv[1], encoding="utf-8", errors="replace") as fh:
        html = fh.read()
    p = Extractor(base)
    p.feed(html)
    p.close()

    body = "\n\n".join(p.blocks)
    out = [body, "", "LINKS IN ARTICLE BODY"]
    for text, href in p.links:
        out.append(f"- [{text}] {href}")
    sys.stdout.write("\n".join(out) + "\n")

    # manifest of dropped material to stderr
    err = []
    err.append(f"BODY BLOCKS: {len(p.blocks)}; BODY LINKS: {len(p.links)}; BODY IMAGES: {p.images}")
    err.append(f"NON-BODY IMAGES DROPPED: {p.dropped_images}")
    err.append("DROPPED TEXT (label: text):")
    for label, text in p.dropped:
        err.append(f"  [{label}] {text}")
    err.append(f"DROPPED LINKS OUTSIDE BODY: {len(p.dropped_links)}")
    for label, _, href in p.dropped_links:
        err.append(f"  [{label}] {href}")
    sys.stderr.write("\n".join(err) + "\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
