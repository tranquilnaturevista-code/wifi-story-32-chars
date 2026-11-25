# Tell a Whole Story in 32 Characters

[![Tell a Whole Story in 32 Characters](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Rank](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/tranquilnaturevista-code/wifi-story-32-chars/rank.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)
[![Reward](https://make.fun/badge/u-xvader-tell-a-whole-story-in-32-characters-f86dd978/tranquilnaturevista-code/wifi-story-32-chars/reward.svg)](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978)

Entry for the [make.fun bounty "Tell a Whole Story in 32 Characters"](https://make.fun/competitions/u-xvader-tell-a-whole-story-in-32-characters-f86dd978) ($2, winner takes all, free to enter). Deadline: 27 Nov 2026, 00:25 WIB.

## What it does

`main.py` writes one original Wi-Fi network name to `/output/entry.txt`:

> SheLeftMeForTheNeighborsWiFi

A whole breakup in 28 characters. She left, the neighbour's Wi-Fi was
the reason — or the better catch — and the narrator is left staring at
his own network list. Three characters (her, him, the neighbour), one
event, and a punchline a stranger gets on the first read. It avoids the
stock Wi-Fi jokes everyone has seen (no FBI van, no "Pretty Fly") and
turns the familiar "neighbour's Wi-Fi" trope into a story instead of a
slogan.

## Run

```sh
python3 main.py   # writes /output/entry.txt (or $OUTPUT_DIR/entry.txt)
```

Deterministic: the same name on every run. The program checks the
competition gate itself before writing — 28 characters of UTF-8 text,
within the 1–32 character gate, not only whitespace — and reads the
file back to confirm it matches byte for byte.
