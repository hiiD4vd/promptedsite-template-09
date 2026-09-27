path_html = r'd:\daud\sourcecode\scrape\balloons\index.html'
with open(path_html, 'r', encoding='utf-8') as f:
    html = f.read()

css_injection = '<style>footer, a[href*="cal.com"], a[href*="shader.se"], img[alt="Shader"] { display: none !important; visibility: hidden !important; pointer-events: none !important; opacity: 0 !important; width: 0 !important; height: 0 !important; }</style></head>'

html = html.replace('</head>', css_injection)

with open(path_html, 'w', encoding='utf-8') as f:
    f.write(html)

print('CSS Injection applied!')
