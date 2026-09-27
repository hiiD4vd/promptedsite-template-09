import os
import re

html_path = r'd:\daud\sourcecode\scrape\balloons\index.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace shader references
html = re.sub(r'Shader Development Studio', 'PromptedSite Studio', html, flags=re.IGNORECASE)
html = re.sub(r'https://shader\.se', 'https://promptedsite.com', html, flags=re.IGNORECASE)
html = html.replace('alt=\\"Shader\\"', 'alt=\\"PromptedSite\\"')
html = html.replace('An experiment by', 'A project by')

# Replace cal.com filip
html = re.sub(r'https://cal\.com/[^/]+/[^\"]+', '#', html, flags=re.IGNORECASE)

# Replace vercel URLs
html = re.sub(r'https://balloons-one\.vercel\.app', 'https://promptedsite.com', html, flags=re.IGNORECASE)

# Replace BALLOONN
html = re.sub(r'BALLOONN spelled with letter balloons', 'PROMPTEDSITE spelled with letter balloons', html, flags=re.IGNORECASE)
html = re.sub(r'Balloon Text Simulation', 'PromptedSite Text Simulation', html, flags=re.IGNORECASE)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Scrubbed index.html metadata and hidden React state!')
