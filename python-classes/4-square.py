#!/usr/bin/python3
"""Write a class Square that defines a square"""
 @property
 def size(self):
     """Retrieve size"""
     return self.__size

 @size.setter
 def size(self, value):
     """Set size with validation"""
     if not isinstance(value, int):
        raise TypeError("size must be an integer")
     if value < 0:
         raise ValueError("size must be >= 0")
     self.__size = value

 def area(self):
     """Return the current square area"""
     return self.__size ** 2

