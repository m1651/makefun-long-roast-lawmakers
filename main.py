#!/usr/bin/env python3
"""The Long Roast: Lawmakers and the File They Cannot Convert - make.fun bounty entry.

Writes a single original sentence (1-320 characters) to /output/entry.txt.
Python 3, stdlib only, no network, fully deterministic.
"""

import os
import sys

MAX_CHARS = 320

LINE = (
    "They can write a 400-page bill regulating artificial intelligence in "
    "a morning, yet by lunch they are still emailing their intern a "
    "crooked photo of a Word document and asking her to please make it "
    "a PDF."
)


def main() -> None:
    # Validate the line before writing: the gate requires UTF-8 text
    # of 1 to 320 characters, not only white space, on a single line,
    # and the brief requires exactly one sentence.
    if not LINE.strip():
        print("error: entry line is empty or only whitespace", file=sys.stderr)
        sys.exit(1)
    if len(LINE) > MAX_CHARS:
        print(
            "error: entry line is %d characters, over the %d limit"
            % (len(LINE), MAX_CHARS),
            file=sys.stderr,
        )
        sys.exit(1)
    if "\n" in LINE or "\r" in LINE:
        print("error: entry line must be a single line", file=sys.stderr)
        sys.exit(1)
    # A judged one-liner must not spend characters on invisible padding:
    # leading or trailing whitespace would count toward the limit.
    if LINE != LINE.strip():
        print(
            "error: entry line must not start or end with whitespace",
            file=sys.stderr,
        )
        sys.exit(1)
    if LINE.count(".") != 1 or not LINE.endswith("."):
        print(
            "error: entry line must be exactly one sentence "
            "(one terminal period)",
            file=sys.stderr,
        )
        sys.exit(1)

    out_path = "/output/entry.txt"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print("wrote %d characters to %s" % (len(LINE), out_path))


if __name__ == "__main__":
    main()
