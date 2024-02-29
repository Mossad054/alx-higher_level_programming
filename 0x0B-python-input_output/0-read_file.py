#!/usr/bin/python3
"""Define a text file-reading function"""


def read_file(filename=""):
    """Prints  contents of  UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
