import os
from glob import glob


def load_rules(paths):
    """
    Load rules
    """
    rules = []
    for path in paths:
        if not os.path.isdir(path):
            print(f"Warning: {path} is not folder. Skipped.")
            continue

        files = glob(os.path.join(path, "*.sexp")) + glob(os.path.join(path, "*.lisp"))
        for file in files:
            with open(file, "r", encoding="utf-8") as f:
                content = f.read()
                rules.append(content)
    return rules
