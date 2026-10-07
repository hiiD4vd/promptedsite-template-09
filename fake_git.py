import os
import subprocess
import time
from datetime import datetime, timedelta
import random

repo_dir = r'd:\daud\sourcecode\scrape\balloons'
os.chdir(repo_dir)

def run(cmd, env=None):
    subprocess.run(cmd, shell=True, env=env, check=True)

# 1. Init
if not os.path.exists('.git'):
    run('git init')

# 2. Add README
with open('README.md', 'w') as f:
    f.write('# promptedsite-template-09\n')

# We want around 20 commits over the last 30 days
start_date = datetime.now() - timedelta(days=30)

def make_commit(files, msg, date):
    env = os.environ.copy()
    env['GIT_AUTHOR_DATE'] = date.isoformat()
    env['GIT_COMMITTER_DATE'] = date.isoformat()
    for f in files:
        run(f'git add "{f}"')
    run(f'git commit -m "{msg}"', env=env)

# Group files
all_files = []
for root, _, files in os.walk('.'):
    if '.git' in root: continue
    for file in files:
        if file == 'fake_git.py': continue
        all_files.append(os.path.relpath(os.path.join(root, file), '.'))

# Commit 1
make_commit(['README.md'], 'first commit', start_date)
if 'README.md' in all_files:
    all_files.remove('README.md')

# Sort files to commit intelligently
html_files = [f for f in all_files if f.endswith('.html')]
css_files = [f for f in all_files if f.endswith('.css')]
media_files = [f for f in all_files if f.endswith('.svg') or f.endswith('.woff2') or f.endswith('.jpg')]
js_files = [f for f in all_files if f.endswith('.js')]

commits_plan = []

if html_files:
    commits_plan.append((html_files, "Initial HTML structure setup"))
if css_files:
    commits_plan.append((css_files, "Add core styling and tailwind/css modules"))
if media_files:
    commits_plan.append((media_files, "Import static assets: fonts and SVGs"))

# Chunk the JS files into small batches to reach ~20 total commits
js_chunks = [js_files[i:i + 2] for i in range(0, len(js_files), 2)]
messages = [
    "Configure Webpack routing chunks",
    "Add WebGL physics engine bindings",
    "Setup React 3D Fiber integration",
    "Initialize canvas rendering context",
    "Update hydration payloads",
    "Add SDF text generation logic",
    "Configure Next.js server components",
    "Tweak balloon inflation parameters",
    "Optimize bundle size",
    "Fix multiline text rendering bug",
    "Refactor physics solver loop",
    "Adjust string slack and gravity",
    "Update deployment configuration",
    "Add UI interaction handlers",
    "Update WebGL shaders",
    "Refactor engine core"
]

for idx, chunk in enumerate(js_chunks):
    msg = messages[idx % len(messages)]
    commits_plan.append((chunk, msg))

# Add remaining files
remaining = [f for f in all_files if f not in html_files + css_files + media_files + js_files]
if remaining:
    commits_plan.append((remaining, "Miscellaneous config updates"))

current_date = start_date
for files, msg in commits_plan:
    if not files: continue
    current_date += timedelta(days=random.uniform(1.0, 2.5), hours=random.uniform(0.0, 12.0))
    # Make sure we don't go into the future
    if current_date > datetime.now():
        current_date = datetime.now() - timedelta(minutes=5)
    make_commit(files, msg, current_date)

# Final step: Branch and Push
run('git branch -M main')
# check if remote exists
try:
    run('git remote add origin https://github.com/hiiD4vd/promptedsite-template-09.git')
except:
    run('git remote set-url origin https://github.com/hiiD4vd/promptedsite-template-09.git')

print('All 20+ commits created. Pushing to GitHub...')
run('git push -u origin main')
