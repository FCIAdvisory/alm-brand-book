#!/usr/bin/env python3
"""Regenerate brand-book.html (self-contained, images embedded) from brand-book/index.html."""
import base64, re, os
os.chdir(os.path.join(os.path.dirname(__file__), '..'))
src = open('brand-book/index.html').read()
def repl(m):
    path = m.group(0).replace('../', '')
    ext = os.path.splitext(path)[1].lstrip('.').lower()
    mime = {'jpg': 'jpeg', 'jpeg': 'jpeg', 'png': 'png'}[ext]
    data = base64.b64encode(open(path, 'rb').read()).decode()
    return f"data:image/{mime};base64,{data}"
out = re.sub(r"\.\./assets/[\w\-.]+", repl, src)
open('brand-book.html', 'w').write(out)
print('brand-book.html', os.path.getsize('brand-book.html'))
