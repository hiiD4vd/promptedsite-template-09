import os
import re
import urllib.request
from urllib.parse import urljoin, urlparse

BASE_URL = 'https://balloons.shader.se'
OUTPUT_DIR = r'd:\daud\sourcecode\scrape\balloons'

def download_file(url, path):
    if os.path.exists(path):
        return True
    os.makedirs(os.path.dirname(path), exist_ok=True)
    print(f"Downloading {url} ...")
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as res:
            with open(path, 'wb') as f:
                f.write(res.read())
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

def extract_urls(text):
    # Match standard URLs starting with / (e.g. /_next/...)
    urls = re.findall(r'\"(/[^\"]+)\"', text)
    urls += re.findall(r'\'(/[^\']+)\'', text)
    # CSS url(/...)
    urls += re.findall(r'url\((/[^\)]+)\)', text)
    # Add anything that looks like a chunk name, e.g. "static/chunks/..."
    chunks = re.findall(r'\"(static/chunks/[^\"]+\.js)\"', text)
    urls += ['/_next/' + c for c in chunks]
    return list(set(urls))

def scrape_recursive():
    queue = ['/']
    visited = set()
    
    while queue:
        current = queue.pop(0)
        if current in visited:
            continue
        visited.add(current)
        
        # Strip query parameters for local saving
        local_path = current.split('?')[0]
        if local_path.endswith('/'):
            local_path += 'index.html'
        if local_path.startswith('/'):
            local_path = local_path[1:]
            
        full_path = os.path.join(OUTPUT_DIR, local_path)
        full_url = urljoin(BASE_URL, current)
        
        success = download_file(full_url, full_path)
        if success and full_path.endswith(('.html', '.js', '.css', '.json')):
            try:
                with open(full_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                new_urls = extract_urls(content)
                for nu in new_urls:
                    if nu not in visited and nu not in queue:
                        # Exclude absolute links outside domain
                        if not nu.startswith('http'):
                            queue.append(nu)
            except Exception as e:
                pass # Binary files

if __name__ == '__main__':
    scrape_recursive()
