import os
import re

dir_path = r'd:\daud\sourcecode\scrape\balloons'

replaced = 0
for root, _, files in os.walk(dir_path):
    for file in files:
        if file.endswith(('.js', '.html')):
            path = os.path.join(root, file)
            try:
                with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                
                new_content = re.sub(r'https://vercel\.live[^\"]+', 'https://promptedsite.com/feedback.js', content, flags=re.IGNORECASE)
                new_content = re.sub(r'__vercel_toolbar', '__promptedsite_toolbar', new_content, flags=re.IGNORECASE)
                
                if new_content != content:
                    with open(path, 'w', encoding='utf-8', errors='ignore') as f:
                        f.write(new_content)
                    replaced += 1
            except:
                pass

print(f'Scrubbed Vercel traces from {replaced} files!')
