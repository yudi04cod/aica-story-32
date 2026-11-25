#!/usr/bin/env python3
"""Write one original Wi-Fi network name (<=32 chars) to /output/entry.txt.

The name is a single fixed string, written by the author in this session.
Deterministic: the same bytes are written on every run.
"""

import os

NAME = "Divorced, He Took The WiFi"

assert 1 <= len(NAME) <= 32, "name must be 1-32 characters"
assert NAME.strip() == NAME, "name must not be only whitespace"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(NAME)
