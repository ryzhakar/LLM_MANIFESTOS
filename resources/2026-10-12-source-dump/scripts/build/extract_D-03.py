# Stdlib-only text extractor for butunclebob.com wiki page (D-03).
# Usage: python3 -I extract_D-03.py <in.html> <out.txt>
# Whole <body> text, script/style dropped, block tags become line breaks, <pre> kept verbatim.
# Wiki chrome is trimmed afterwards by extract step (see report), not by this script.
import sys, re
from html.parser import HTMLParser

BLOCK = {"p", "div", "br", "h1", "h2", "h3", "h4", "h5", "li", "tr", "ul", "ol", "table", "dt", "dd", "blockquote", "hr"}

class Ext(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out = []
        self.skip = 0
        self.inbody = False
    def handle_starttag(self, tag, attrs):
        if tag == "body":
            self.inbody = True
        if tag in ("script", "style", "noscript"):
            self.skip += 1
            return
        if not self.inbody:
            return
        if tag in BLOCK:
            self.out.append("\n")
    def handle_endtag(self, tag):
        if tag == "body":
            self.inbody = False
        if tag in ("script", "style", "noscript"):
            self.skip = max(0, self.skip - 1)
            return
        if tag in BLOCK:
            self.out.append("\n")
    def handle_data(self, data):
        if self.inbody and not self.skip:
            self.out.append(data)

def main():
    src, dst = sys.argv[1], sys.argv[2]
    text = open(src, "rb").read().decode("utf-8", errors="replace")
    p = Ext()
    p.feed(text)
    s = "".join(p.out)
    lines = [re.sub(r"[ \t\r\f\v\xa0]+", " ", ln).strip() for ln in s.split("\n")]
    body = []
    for ln in lines:
        if ln == "" and (not body or body[-1] == ""):
            continue
        body.append(ln)
    open(dst, "w", encoding="utf-8").write("\n".join(body).strip() + "\n")

main()
