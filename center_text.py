import re

path = r'd:\daud\sourcecode\scrape\balloons\_next\static\immutable\chunks\215-ommkx982a-v2.js'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('a.textAlign="left"', 'a.textAlign="center"')
text = re.sub(r'a\.fillText\(L,h\+c\.actualBoundingBoxLeft,', r'a.fillText(L,p/2,', text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Text rendering horizontally centered!')
