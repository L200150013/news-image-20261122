#!/usr/bin/env python3
"""news-image-20261122 entrypoint.

Writes the front-page image for Sunday 22 November 2026 to the output
directory. The image is shipped in this repository as entry.png and is
copied verbatim: no network, no clock, no randomness, so two runs write
byte-identical files.

Standard library only.
"""

import os
import shutil
import sys

IMAGE_NAME = "entry.png"


def output_dir():
    """Grader output directory: MAKEFUN_OUTPUT_DIR, else /output."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, IMAGE_NAME)
    if not os.path.isfile(src):
        sys.stderr.write("entry.png missing from repository\n")
        return 1
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    # Empty the output directory's contents only. /output on the grader
    # is a mount point: never remove the directory itself.
    for name in os.listdir(out):
        path = os.path.join(out, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    shutil.copyfile(src, os.path.join(out, IMAGE_NAME))
    # The copy must be byte-identical to the shipped image.
    if os.path.getsize(os.path.join(out, IMAGE_NAME)) != os.path.getsize(src):
        sys.stderr.write("copied entry.png size mismatch\n")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
