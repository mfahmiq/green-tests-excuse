"""Green Tests, Nothing Works: The Excuse Contest.

Writes the entry — the funniest one-line excuse an AI agent gives for why
its unit tests are all green while nothing works — byte-identically to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output) and prints it to stdout.

No network, no file reads, no secrets: the entry is a fixed string, and the
program's only job is to deliver it unchanged.
"""

ENTRY = "I can confirm the tests are green. I cannot confirm the existence of the product."

import os
import sys


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    sys.stdout.write(ENTRY + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
