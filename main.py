#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Writes one sentence (at most 200 characters) pitching a bizarre startup
idea that sounds like a joke yet holds together as a real business, to
/output/entry.txt, for make.fun's bounty of the same name.

The program holds a short ranked list of hand-written pitches, each one
checked against the brief: a single sentence, 1-200 characters, naming
the odd thing being sold, who pays for it, and why the money makes sense.
The first pitch that passes every check is written out. No network, no
clock, no randomness: two runs produce byte-identical output.
"""

import os
import sys

# Ranked pitches, best first. Each is one sentence: the odd thing sold,
# the customer who pays, and the reason the absurd premise is a real market.
PITCHES = [
    # A funeral for a plant: ridiculous at first glance, but plant parents
    # are a real market and $29 buys dignity instead of the bin.
    "We throw tiny funerals for dead houseplants, because grieving plant "
    "parents pay $29 for a miniature coffin, a eulogy, and a guilt-free "
    "goodbye instead of the bin.",
    # Retired sniffer dogs as date vetting: strange, concrete, and singles
    # pay to learn the truth before dessert.
    "We rent retired sniffer dogs as first-date lie detectors, because "
    "singles pay $49 to learn before dessert whether their date is hiding "
    "a spouse, a felony, or a timeshare.",
    # A backup culture for a named starter: bakers already treat the jar
    # like a pet, so a revival hotline is a subscription, not a gag.
    "We sell backup sourdough starters with a 24-hour revival hotline, "
    "because bakers who named their starter pay $4 a month to never mourn "
    "a jar of flour and water again.",
]

MAX_CHARS = 200
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def is_valid_pitch(text):
    """A pitch is valid when it is one sentence of 1-200 characters."""
    if not isinstance(text, str):
        return False
    stripped = text.strip()
    if not stripped or len(stripped) > MAX_CHARS:
        return False
    # One flat line: no embedded newline, tab, or doubled space.
    if any(ch in stripped for ch in ("\n", "\r", "\t")) or "  " in stripped:
        return False
    # Exactly one sentence: a single terminal full stop, at the very end.
    if not stripped.endswith("."):
        return False
    if stripped[:-1].count(".") != 0:
        return False
    return True


def pick_pitch():
    """Return the first pitch that passes every check, or None."""
    for pitch in PITCHES:
        if is_valid_pitch(pitch):
            return pitch.strip()
    return None


def main():
    pitch = pick_pitch()
    if pitch is None:
        print("error: no valid pitch available", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(pitch)
    print(pitch)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
