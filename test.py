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
        result = subprocess.run(['pip', 'install', '-r', 'requirements.txt'], capture_output=True, text=True)
        if result.returncode != 0:
            print("Error installing requirements")
            print("stdout:", result.stdout)
            print("stderr:", result.stderr)
            raise Exception(f"Failed to install requirements in {module_dir}")

    result = subprocess.run(['python', 'test.py'], capture_output=True, text=True)
    if result.returncode != 0:
        print("Test failed")
        print("stdout:", result.stdout)
        print("stderr:", result.stderr)
        raise Exception(f"Test failed in {module_dir}")

    os.chdir('..')
    print(f"Exiting {module_dir}")
