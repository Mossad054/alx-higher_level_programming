#!/usr/bin/python3
"""Define  function that adds attributes to objects."""


def add_attribute(obj, att, value):
    """Add a new attribute to an object.

    Args:
        obj (any):  object to add an attribute.
        att (str):  name of the attribute to add to obj.
        value (any): value of attributes.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
