#!/usr/bin/env python3
"""Rename the Planet - make.fun entry 286.

Writes a single line (under 200 characters) to /output/entry.txt:
a funny new name for a planet of our solar system, plus the why,
in the same breath. A house judge compares lines two at a time on
how funny the joke is, whether the why earns the name, how fresh
the angle is and how tight the wording is.

Pure standard library only. Fully deterministic: running it twice
produces byte-identical output.
"""

import os

ENTRY = (
    "Neptune is now 'The Group Chat Ghost' because it takes 165 years "
    "to reply, and when it does, it's just blue ticks."
)


def main():
    line = ENTRY.strip()
    assert 1 <= len(line) <= 200, "entry must be 1-200 chars, got %d" % len(line)
    assert line.strip(), "entry must not be only whitespace"
    assert "\n" not in line, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
