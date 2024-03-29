#!/usr/bin/python3
"""Defines a file-appending function."""


def append_write(filename="", text=""):
    """Append string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): strings to append to the file.
    Returns:
        num of characters appended
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text
