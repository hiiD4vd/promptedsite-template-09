import re
paths = [
    r'd:\daud\sourcecode\scrape\balloons\_next\static\immutable\chunks\215-ommkx982a.js',
    r'd:\daud\sourcecode\scrape\balloons\_next\static\immutable\chunks\3r5716256bwc-.js',
    r'd:\daud\sourcecode\scrape\balloons\_next\static\immutable\chunks\1nj36koo1aehk.js'
]
for p in paths:
    with open(p, 'r', encoding='utf-8', errors='ignore') as f:
        text = f.read()
        # Look for the exact word 'SHADER' or 'shader' in quotes
        matches = re.finditer(r'([\'\"`])(shader|SHADER)([\'\"`])', text)
        for m in matches:
            print(f'Exact string match in {p[-15:]}:', text[max(0, m.start()-20):m.end()+20])
