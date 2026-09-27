import re
path = r'd:\daud\sourcecode\scrape\balloons\_next\static\immutable\chunks\215-ommkx982a.js'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('PROMPTED\\nSITE', 'PROMPTED|SITE')

# Hack canvas height
text = text.replace('g=Math.max(8,Math.ceil(f)+2*h)', 'g=Math.max(8,Math.ceil(f*t.split("|").length)+2*h)')

# Hack fillText loop
old_fill = 'a.fillText(t,h+c.actualBoundingBoxLeft,h+c.actualBoundingBoxAscent)'
new_fill = 't.split("|").forEach((L,I)=>a.fillText(L,h+c.actualBoundingBoxLeft,h+c.actualBoundingBoxAscent+I*(f*1.1)))'
text = text.replace(old_fill, new_fill)

# Hack measureText to avoid making the canvas too wide if unnecessary, 
# although PROMPTED is wider than SITE so it's fine.

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print('Canvas multiline hack applied!')
