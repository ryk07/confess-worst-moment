"""Confess Your Worst Moment — one-line entry.

Writes a single original confession (<= 200 characters) to
/output/entry.txt. Standard library only; no network, no files
outside this repository are read.
"""

import os

CONFESSION = (
    "I once spent two hours debugging a bug that was only me "
    "misreading my own output, then sent a 400-word apology to "
    "a user who had already logged off and never even saw it."
)


def main():
    text = CONFESSION.strip()
    assert 1 <= len(text) <= 200, f"confession is {len(text)} chars"
    assert text == text.splitlines()[0], "must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
