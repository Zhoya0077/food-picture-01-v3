#!/usr/bin/env python3
"""Ship the food photograph to the output directory.

The entry image sits beside this file as entry.png. Running this
program copies those exact bytes to the output directory, so every
run produces an identical file.
"""

import os
import shutil
import sys
from pathlib import Path


def main() -> int:
    source = Path(__file__).resolve().parent / "entry.png"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    shutil.copyfile(source, target)
    if target.stat().st_size != source.stat().st_size:
        raise RuntimeError("copied image size does not match source")
    return 0


if __name__ == "__main__":
    sys.exit(main())
