import os
import subprocess

def get_submodule_paths():
    submodule_paths = []
    with open('.gitmodules') as file:
        for line in file:
            if 'path =' in line:
                path = line.strip().split('= ')[1]
                submodule_paths.append(path)
    return submodule_paths

submodule_paths = get_submodule_paths()

for module_dir in submodule_paths:
    os.chdir(module_dir)
    print(f"Entering {module_dir}")
    if os.path.isfile('requirements.txt'):
        subprocess.run(['pip', 'install', '-r', 'requirements.txt'], check=True)
    subprocess.run(['python', 'test.py'], check=True)
    os.chdir('..')
    print(f"Exiting {module_dir}")
