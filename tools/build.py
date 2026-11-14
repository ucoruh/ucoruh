"""Builds index.html from the design template.
Usage: py -3.12 tools/build.py <template.html> <photo.b64> [out=index.html]
Fills {{FOTO}}, {{TEZ_DR_URL}}, {{TEZ_YL_URL}}; wraps the fragment in a full HTML document
(SEO/OG meta, favicon/fonts/styles in <head>)."""
import re
import sys
from pathlib import Path

TEZ = "https://tez.yok.gov.tr/UlusalTezMerkezi/tarama.jsp"
DESC = ("Asst. Prof. Dr. Uğur Coruh — Recep Tayyip Erdoğan University, Computer Engineering. "
        "Applied, post-quantum and white-box cryptography, V2X security, smart cards and payment systems.")

tpl, photo = sys.argv[1], sys.argv[2]
out = Path(sys.argv[3] if len(sys.argv) > 3 else Path(__file__).resolve().parent.parent / "index.html")
h = Path(tpl).read_text(encoding="utf-8")
for k in ("{{FOTO}}", "{{TEZ_DR_URL}}", "{{TEZ_YL_URL}}"):
    assert h.count(k) == 1, f"{k} count {h.count(k)}"
h = h.replace("{{FOTO}}", Path(photo).read_text().strip()).replace("{{TEZ_DR_URL}}", TEZ).replace("{{TEZ_YL_URL}}", TEZ)
h = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\s*', "", h)
h = re.sub(r"<title>.*?</title>", "<title>Dr. Uğur Coruh</title>", h, count=1)
first = h.index("<div")  # everything before the first element (title, links, styles) goes to <head>
head = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="{DESC}">
<meta property="og:title" content="Dr. Uğur Coruh">
<meta property="og:description" content="{DESC}">
<meta property="og:url" content="https://www.ugurcoruh.com/">
<link rel="canonical" href="https://www.ugurcoruh.com/">
<style>[hidden]{{display:none!important}}img{{max-width:100%}}:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0}}</style>
"""
out.write_text(head + h[:first] + "</head>\n<body>\n" + h[first:] + "\n</body>\n</html>\n", encoding="utf-8")
print(out, round(out.stat().st_size / 1024), "KB")
