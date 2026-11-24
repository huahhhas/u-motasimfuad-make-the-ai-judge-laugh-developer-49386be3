#!/usr/bin/env python3
"""Entry for make.fun bounty u-motasimfuad-make-the-ai-judge-laugh-developer-49386be3.

Writes one funny single-line excuse a developer gives when code breaks in
production to $OUTPUT_DIR/entry.txt (default /output), with no trailing
newline, then self-verifies the written file.
"""

import hashlib
import os
import sys

LINE = "It worked on my machine, which runs on hope, cached credentials, and a fan that hasn't spun since 2019."


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)

    # Self-verify the written file: UTF-8, 1-200 characters, not only
    # whitespace, exact match with the intended line, no trailing newline,
    # byte-identical to what we meant to write.
    with open(path, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not match expected line"
    assert not text.endswith("\n"), "trailing newline present"
    assert raw == data, "written bytes differ from expected"
    print(f"OK: wrote {len(raw)} bytes, {len(text)} chars to {path}")
    print(f"sha256: {hashlib.sha256(raw).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
