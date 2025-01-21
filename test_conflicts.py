import os
import ast

class FunctionConflictVisitor(ast.NodeVisitor):
    def __init__(self):
        self.functions = {}
        self.conflicts = []

    def visit_FunctionDef(self, node):
        if node.name in self.functions:
            self.conflicts.append((node.name, self.functions[node.name], (node.lineno, node.col_offset)))
        else:
            self.functions[node.name] = (node.lineno, node.col_offset)
        self.generic_visit(node)

def find_conflicts(directory):
    conflicts = []
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    tree = ast.parse(f.read(), filename=file)
                    visitor = FunctionConflictVisitor()
                    visitor.visit(tree)
                    if visitor.conflicts:
                        conflicts.extend([(file, conflict[0], conflict[1], conflict[2]) for conflict in visitor.conflicts])
    
    return conflicts

if __name__ == "__main__":
    conflicts = find_conflicts('.')
    if conflicts:
        for file, func_name, (line1, col1), (line2, col2) in conflicts:
            print(f"Conflict found in {file}:\n  Function '{func_name}' at line {line1}, column {col1}\n  Conflict with definition at line {line2}, column {col2}")
        exit(1)
    else:
        print("No conflicts found.")
        exit(0)
