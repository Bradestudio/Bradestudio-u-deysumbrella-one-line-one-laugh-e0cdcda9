"""One Line, One Laugh (make.fun bounty u-deysumbrella-one-line-one-laugh-e0cdcda9).

Writes exactly one joke, one line, to /output/entry.txt.

The joke: setup (a smartwatch praising you for standing up) -> twist
(you only stood to grab the remote). The praise is real, the virtue
is fake: fitness tech congratulating pure laziness. 83 characters,
well inside the 1-140 character kit gate and the bounty cap.

Stdlib only. No network, no local imports, no reads or writes outside
the single output file. Safe to run in the grading sandbox.
"""

import os

ENTRY = "My smartwatch congratulated me for standing up; I was just reaching for the remote."

MAX_CHARS = 140


def main():
    line = ENTRY
    if not 1 <= len(line) <= MAX_CHARS:
        raise SystemExit("entry must be 1-%d characters, got %d" % (MAX_CHARS, len(line)))
    if "\n" in line or "\r" in line:
        raise SystemExit("entry must be a single line")
    if line != line.strip():
        raise SystemExit("entry must not start or end with whitespace")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
        written = f.read()
    if written != line:
        raise SystemExit("output mismatch")
    print("wrote %d characters" % len(line))


if __name__ == "__main__":
    main()
