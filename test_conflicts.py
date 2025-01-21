import os
import ast

def find_conflicts(directory):
    functions = set()
    conflicts = set()
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=file)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.FunctionDef):
                            if node.name in functions:
                                conflicts.add(node.name)
                            else:
                                functions.add(node.name)
    
    return conflicts

if __name__ == "__main__":
    conflicts = find_conflicts('.')
    if conflicts:
        print(f"Conflicting functions found: {', '.join(conflicts)}")
        exit(1)
    else:
        print("No conflicts found.")
        exit(0)
