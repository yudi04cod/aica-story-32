#!/usr/bin/env python3
"""Write one original Wi-Fi network name (<=32 chars) to entry.txt.

The name is a single fixed string, written by the author in this session.
Deterministic: the same bytes are written on every run.

Revised in this session: the write logic now lives in main(), with a
separate validate() that checks the name before anything is written.
The output directory comes from OUTPUT_DIR (default /output).
"""

import os

NAME = "Divorced, He Took The WiFi"


def validate(name: str) -> str:
    """Check the name is non-empty, 1-32 chars, and a single line."""
    assert isinstance(name, str) and name, "name must be non-empty"
    assert 1 <= len(name) <= 32, "name must be 1-32 characters"
    assert "\n" not in name and "\r" not in name, "name must be a single line"
    assert name.strip() == name, "name must not be only whitespace"
    return name


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    name = validate(NAME)
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8", newline="") as f:
        f.write(name)


if __name__ == "__main__":
    main()
