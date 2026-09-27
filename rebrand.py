import re

# 1. Patch 215-ommkx982a.js
path_js = r'd:\daud\sourcecode\scrape\balloons\_next\static\immutable\chunks\215-ommkx982a.js'
with open(path_js, 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'(text:[\'\"])SHADER([\'\"])', r'\g<1>PROMPTEDSITE\g<2>', text)

with open(path_js, 'w', encoding='utf-8') as f:
    f.write(text)

# 2. Patch index.html
path_html = r'd:\daud\sourcecode\scrape\balloons\index.html'
with open(path_html, 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<title>Balloon Text Simulation | Shader Development Studio</title>', '<title>PROMPTEDSITE</title>')
html = re.sub(r'<footer.*?</footer>', '<footer></footer>', html, flags=re.DOTALL)

with open(path_html, 'w', encoding='utf-8') as f:
    f.write(html)

# 3. Patch logo.svg (just empty it)
path_svg = r'd:\daud\sourcecode\scrape\balloons\logo.svg'
with open(path_svg, 'w', encoding='utf-8') as f:
    f.write('<svg xmlns="http://www.w3.org/2000/svg"></svg>')

print('Rebranding complete!')
