import os


def load_tasklists(file_paths):
    """
    Load one or multiple tasklist files and combine into a single string.
    """
    all_tasks = []
    for path in file_paths:
        if not os.path.isfile(path):
            print(f"Tasklist faili ei leitud: {path}. Skipped.")
            continue
        with open(path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if content:
                all_tasks.append(content)
    if not all_tasks:
        return None
    return "\n\n".join(all_tasks)
