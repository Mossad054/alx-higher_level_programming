#!/usr/bin/python3
"""Define file-writing function."""


def write_file(filename="", text=""):
    """Write a string to UTF8 text file.

    Args:
        filename (str): name of the file to write.
        text (str):txt output
    Return:
         number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
