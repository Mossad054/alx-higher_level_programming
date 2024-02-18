#!/usr/bin/python3
"""Defines a locked class."""


class LockedClass:
    """
    Prevent user from instantiating  LockedClass attributes
    for anything but only attribute when called 'first_name'.
    """

    __slots__ = ["first_name"]
