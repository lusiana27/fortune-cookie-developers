"""Fortune Cookie Wisdom for Developers.

Writes one original fortune-cookie line for a software developer
to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Standard library only. Never deletes the output folder itself.
"""

import os

LINE = "Beware the shortcut: today it saves an hour, tomorrow it becomes the legacy you inherit."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    # Clear only the contents of the output folder, never the folder.
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        # The gate allows 1 to 120 characters; refuse to write an overlong line.
        assert 1 <= len(LINE) <= 120, len(LINE)
        f.write(LINE)


if __name__ == "__main__":
    main()
