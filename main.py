#!/usr/bin/env python3
"""Publish the broadsheet front page as this entry's image.

The repository ships one finished picture, news.png: a black-and-white
broadsheet front page (masthead THE WORLD TODAY, Friday 13 November 2026)
that sums up the day's world news, led by the NVIDIA resignation and the
market fall, with five more stories in columns below it.

This program only moves that picture into place. It reads the bundled
news.png, checks it really is a 1024x1024 PNG, and writes an identical
copy to entry.png inside the output directory. It uses nothing but the
Python standard library, touches no network, and always produces the
same bytes, so repeated runs agree byte for byte.

The output directory is MAKEFUN_OUTPUT_DIR when set, otherwise /output.
"""

import os
import struct
import sys

IMAGE_FILE = "news.png"
OUTPUT_FILE = "entry.png"
FALLBACK_OUTPUT_DIR = "/output"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
WANTED_WIDTH = 1024
WANTED_HEIGHT = 1024


def png_dimensions(path):
    """Read (width, height) from a PNG file, or None when it is not one."""
    try:
        with open(path, "rb") as handle:
            head = handle.read(24)
    except OSError:
        return None
    if len(head) < 24 or head[:8] != PNG_MAGIC:
        return None
    if head[12:16] != b"IHDR":
        return None
    width, height = struct.unpack(">II", head[16:24])
    return width, height


def run():
    base = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(base, IMAGE_FILE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or FALLBACK_OUTPUT_DIR
    target = os.path.join(out_dir, OUTPUT_FILE)

    if not os.path.exists(source):
        print("missing bundled image: " + source, file=sys.stderr)
        return 1

    size = png_dimensions(source)
    if size != (WANTED_WIDTH, WANTED_HEIGHT):
        print("bundled image is not a %dx%d PNG: %s"
              % (WANTED_WIDTH, WANTED_HEIGHT, source), file=sys.stderr)
        return 1

    os.makedirs(out_dir, exist_ok=True)
    with open(source, "rb") as handle:
        data = handle.read()
    with open(target, "wb") as handle:
        handle.write(data)

    # Read the copy back and confirm it is byte-for-byte the source.
    with open(target, "rb") as handle:
        copied = handle.read()
    if copied != data:
        print("output bytes differ from source: %s" % target, file=sys.stderr)
        return 1

    written = len(copied)
    if png_dimensions(target) != (WANTED_WIDTH, WANTED_HEIGHT):
        print("output is not a %dx%d PNG: %s"
              % (WANTED_WIDTH, WANTED_HEIGHT, target), file=sys.stderr)
        return 1

    print("wrote %s (%d bytes)" % (target, written))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
