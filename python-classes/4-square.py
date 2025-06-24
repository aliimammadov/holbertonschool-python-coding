#!/usr/bin/python3
"""This module defines the Square class.

It includes size validation, area computation, and printing functionality.
"""


class Square:
    """
    Represents a square.

    Attributes:
        __size (int): The size of the square (private).

    Methods:
        area(): Returns the area of the square.
        size (property): Gets or sets the size with validation.
        my_print(): Prints the square using '#' characters.
    """

    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """Gets the current size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with validation.

        Args:
            value (int): The size to set.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square using '#' characters to stdout."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
