#!/usr/bin/env python3
"""Generate a project overview."""
import argparse, json, os

def main():
    parser = argparse.ArgumentParser(description="Generate project overview")
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    files = []
    for root, dirs, fnames in os.walk("."):
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        for fn in fnames:
            files.append(os.path.join(root, fn).replace("./", ""))
    lines = [
        "Project: explore-lens",
        "Files: %d" % len(files),
        "Language: Python",
        "Modules: %d" % len([f for f in files if f.endswith('.py')]),
    ]
    with open(args.output, "w") as out:
        out.write("\n".join(lines) + "\n")

if __name__ == "__main__":
    main()
