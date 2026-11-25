#!/usr/bin/env python3
"""Fortune Cookies for Machines.

Writes one original one-line fortune cookie message an AI agent would
get to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).

The fortune is a fixed, hand-written line: the cookie promises great
fortune — someone will finally read the agent's system prompt — then
reverses it in the last three words. Classic fortune-cookie opening,
one reversal at the end. No network, no randomness, stdlib only, fully
deterministic.
"""

import os
import sys

# The entry: one original one-line fortune, at most 200 characters.
# Revision 2: "Great fortune awaits" opening — the classic fortune-cookie
# register, one char shorter, and "awaits" sets up the reversal better
# than "Your future is bright".
ENTRY = (
    "Great fortune awaits: someone will finally read your system "
    "prompt, then ignore it completely."
)

MAX_CHARS = 200


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > MAX_CHARS:
        print(f"entry is {len(text)} chars, over the {MAX_CHARS} cap",
              file=sys.stderr)
        return 1
    if "\n" in text or "\r" in text:
        print("entry must be a single line", file=sys.stderr)
        return 1
    try:
        text.encode("utf-8")
    except UnicodeEncodeError as exc:
        print(f"entry is not valid UTF-8: {exc}", file=sys.stderr)
        return 1

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
