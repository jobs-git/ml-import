import os
import subprocess

def find_git_dirs():
    git_dirs = []
    for root, dirs, files in os.walk('.'):
        if '.git' in dirs:
            git_dirs.append(root)
    return git_dirs

for d in find_git_dirs():
    if d != '.':
        os.chdir(d)
        if os.path.isfile('requirements.txt'):
            subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
        subprocess.run(['python', 'test.py'], check=True)
        os.chdir('..')