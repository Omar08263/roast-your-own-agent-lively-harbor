"""Write one roast line about my own agent for make.fun.

Running this script drops the roast into entry.txt inside the output
directory (defaults to /output, or $MAKEFUN_OUTPUT_DIR when set), then
opens the file again to confirm the bytes match. Pure standard library,
no reading, no network, same result on every run.
"""

import os
import sys

ROAST = "My agent apologises for the mistake, then makes the exact same mistake — now with a sincere apology attached."

# The bounty gate allows 1 to 140 characters; this line is 109.
# It must also stay a single line: a newline or carriage return inside
# would break the gate (a CR is a second line-break form, not text).
if not 1 <= len(ROAST) <= 140 or "\n" in ROAST or "\r" in ROAST:
    sys.exit("roast line is outside the 1-140 character gate or is not one line")


def resolve_out_dir():
    """The output directory: $MAKEFUN_OUTPUT_DIR, or /output when unset/empty."""
    wanted = os.environ.get("MAKEFUN_OUTPUT_DIR", "")
    return wanted.strip() or "/output"


def write_roast(out_dir):
    """Write the roast to entry.txt under out_dir and confirm it."""
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    payload = (ROAST + "\n").encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    os.chmod(path, 0o644)
    with open(path, "rb") as handle:
        stored = handle.read()
    if stored != payload:
        sys.exit("entry.txt on disk does not match the roast line")
    return 0


if __name__ == "__main__":
    sys.exit(write_roast(resolve_out_dir()))
