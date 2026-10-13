# Stdlib-only text extractor for EWD447 transcription (D-02).
# Usage: python3 -I extract_D-02.py <in.html> <out.txt>
# Keeps the text of the #content div in order; paragraphs become blank-line separated.
import sys, re
from html.parser import HTMLParser

BLOCK = {"p", "div", "br", "h1", "h2", "h3", "h4", "li", "tr", "blockquote", "pre"}

class Ext(HTMLParser):
    def __init__(self, root_id):
        super().__init__(convert_charrefs=True)
        self.root_id = root_id
        self.capturing = False
        self.depth = 0          # div depth inside root
        self.out = []
        self.skip = 0
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if not self.capturing:
            if a.get("id") == self.root_id:
                self.capturing = True
                self.depth = 1
            return
        if tag == "div":
            self.depth += 1
        if tag in ("script", "style"):
            self.skip += 1
        if tag in BLOCK:
            self.out.append("\n")
    def handle_endtag(self, tag):
        if not self.capturing:
            return
        if tag in ("script", "style"):
            self.skip = max(0, self.skip - 1)
        if tag == "div":
            self.depth -= 1
            if self.depth == 0:
                self.capturing = False
                return
        if tag in BLOCK:
            self.out.append("\n")
    def handle_data(self, data):
        if self.capturing and not self.skip:
            self.out.append(data)

def main():
    src, dst = sys.argv[1], sys.argv[2]
    raw = open(src, "rb").read()
    text = raw.decode("iso-8859-1")  # page declares charset=ISO-8859-1
    p = Ext("content")
    p.feed(text)
    s = "".join(p.out)
    lines = [re.sub(r"[ \t\r\f\v]+", " ", ln).strip() for ln in s.split("\n")]
    body = []
    for ln in lines:
        if ln == "" and (not body or body[-1] == ""):
            continue
        body.append(ln)
    open(dst, "w", encoding="utf-8").write("\n".join(body).strip() + "\n")

main()
