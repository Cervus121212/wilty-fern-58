#!/usr/bin/env python3
"""Unsent: The Micro-Confession Sprint — one two-part micro-confession.

Writes the unsent message (a To: line and the unsent line itself) to
$MAKEFUN_OUTPUT_DIR/entry.txt as UTF-8 text, no trailing newline.

Gate: exactly two parts, 1-260 characters total, message line <= 200 chars.
"""

import os

ENTRY = (
    "To: my grandma's neighbour, who still waters her plants\n"
    "i told you she was just visiting family, and i have let you keep "
    "watering a dead woman's plants for eight months because i cannot "
    "say it out loud"
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
