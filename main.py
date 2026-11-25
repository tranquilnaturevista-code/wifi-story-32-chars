#!/usr/bin/env python3
"""Tell a Whole Story in 32 Characters — entry program.

Writes one original Wi-Fi network name to /output/entry.txt (or
$OUTPUT_DIR/entry.txt). The name is fixed and hand-written for this
bounty; the program checks it against the competition gate before
writing: UTF-8 text of 1 to 32 characters, not only whitespace.

The name: SheLeftMeForTheNeighborsWiFi (28 characters)

A whole breakup in one network name: she left, the neighbour's Wi-Fi
was the reason (or the better catch), and the narrator is left staring
at his own network list. Three characters — her, him, the neighbour —
one event, and a punchline a stranger gets on the first read, with no
explanation needed. It dodges the stock Wi-Fi jokes (no FBI van, no
"Pretty Fly") and turns the familiar "neighbour's Wi-Fi" trope into a
story instead of a slogan. The joke lands twice: once for the narrator
who has to live with it, and once for every neighbour who spots it
while scrolling their own list of available networks.
"""

import os
import sys

NAME = "SheLeftMeForTheNeighborsWiFi"


def check_gate(text):
    """Return a list of gate failures; empty means the entry is valid."""
    problems = []
    if not text.strip():
        problems.append("entry is blank")
    size = len(text.encode("utf-8"))
    if not 1 <= size <= 32:
        problems.append(
            "entry is %d UTF-8 characters, gate needs 1-32" % size
        )
    return problems


def main():
    problems = check_gate(NAME)
    if problems:
        for problem in problems:
            print("gate failure: " + problem, file=sys.stderr)
        sys.exit(1)

    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(NAME)

    with open(path, encoding="utf-8") as handle:
        written = handle.read()
    if written != NAME:
        print("entry mismatch after write", file=sys.stderr)
        sys.exit(1)
    # Re-check the gate against what actually landed on disk, so a
    # write that silently changed the text can never pass quietly.
    problems = check_gate(written)
    if problems:
        for problem in problems:
            print("gate failure on disk: " + problem, file=sys.stderr)
        sys.exit(1)

    print(
        "Wrote entry.txt: %r, %d characters"
        % (written, len(written.encode("utf-8")))
    )


if __name__ == "__main__":
    main()
