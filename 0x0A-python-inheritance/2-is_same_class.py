#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is exactly an instance of a given class.

    Args:
        obj (any): The object checked
        a_class (type): class matched to the type of obj.
    Returns:
        If obj is an instance of a_class i.e True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False
