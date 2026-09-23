from pathlib import Path


def list_directory(path: str = ".") -> str:
    folder = Path(path)

    if not folder.exists():
        return f"Path not found: {path}"

    if not folder.is_dir():
        return f"Not a folder: {path}"

    items = []

    for item in folder.iterdir():
        if item.is_dir():
            items.append(f"[FOLDER] {item.name}")
        else:
            items.append(f"[FILE] {item.name}")

    if not items:
        return "Folder is empty."

    return "\n".join(sorted(items))


def path_exists(path: str) -> str:
    target = Path(path)

    if target.exists():
        if target.is_dir():
            return f"Folder exists: {path}"
        return f"File exists: {path}"

    return f"Path does not exist: {path}"