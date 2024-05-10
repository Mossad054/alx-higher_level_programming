#!/usr/bin/python3
"""Defines  peak problem"""


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    size = len(list_of_integers)
    if size == 1:
        return list_of_integers[0]
    elif size == 2:
        return max(list_of_integers)

    md = int(size / 2)
    pk = list_of_integers[md]
    if pk > list_of_integers[md - 1] and pk > list_of_integers[md + 1]:
        return pk
    elif pk < list_of_integers[md - 1]:
        return find_peak(list_of_integers[:md])
    else:
        return find_peak(list_of_integers[md + 1:])
