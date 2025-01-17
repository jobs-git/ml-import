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
    print(f"Entering {module_dir}")
    if os.path.isfile(os.path.join(module_dir, 'requirements.txt')):
        subprocess.run(['pip', 'install', '-r', os.path.join(module_dir, 'requirements.txt')], check=True)
    subprocess.run(['python', os.path.join(module_dir, 'test.py')], check=True)
