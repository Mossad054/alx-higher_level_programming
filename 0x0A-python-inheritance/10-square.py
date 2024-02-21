#!/usr/bin/python3

"""importing BaseGeometry & Rectangle"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

"""Writes a class squarewhich inherites from rectangle"""


class Square(Rectangle):
    """A subclass of Rectangle class"""
    def __init__(self, size):
        """initializes private attribute size and validate it"""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """return area of a square"""
        return self.__size ** 2
