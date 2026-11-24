"""Everyday Wonder, Two Days to Find the Line — make.fun entry.

One sentence, at most 200 characters, on a small moment of wonder in
everyday life: a bus braking, and every passenger's reflection sliding
forward in the window, arriving a second before we do.

Running this script prints the sentence to stdout and, when the harness
variable MAKEFUN_OUTPUT_DIR is set, writes it (with no trailing
newline) to <MAKEFUN_OUTPUT_DIR>/entry.txt.
"""

import os

SENTENCE = "The bus braked, and every passenger's reflection slid forward in the window, arriving a second before we did."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(SENTENCE)
    print(SENTENCE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
