import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
EXCLUDED_DIRS = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    "node_modules",
    "build",
    "dist",
    ".idea",
}

def read_json_files(root: Path):
    files = []

    for path in root.rglob("*.json"):
        relative_parts = path.relative_to(root).parts
        if any(part in EXCLUDED_DIRS for part in relative_parts):
            continue
        files.append(path)

    results = {}

    for file_path in sorted(files):
        try:
            with file_path.open("r", encoding="utf-8") as f:
                data = json.load(f)
            results[str(file_path.relative_to(root))] = data
            print(f"Loaded: {file_path.relative_to(root)}")
        except Exception as e:
            print(f"Could not read {file_path.relative_to(root)}: {e}")

    return results


def main():
    all_json_data = read_json_files(REPO_ROOT)

    for filename, data in all_json_data.items():
        print(f"\n--- {filename} ---")
        print(json.dumps(data, ensure_ascii=False, indent=2)[:2000])  # preview only

    print(f"\nTotal JSON files read: {len(all_json_data)}")


if __name__ == "__main__":
    main()
