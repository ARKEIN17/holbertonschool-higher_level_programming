<<<<<<< HEAD
#!/usr/bin/python3
"""
Contains the class MyInt
"""


Rectangle = __import__('9-rectangle').Rectangle
""" module with class BaseGeometry """


class Square(Rectangle):
    """Square class that inherits from Rectangle that inherits BaseGeometry"""

    def __init__(self, size):
        """Method for initialized the attrubutes"""

        super().__init__(size, size)
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """rectangle area"""

        return self.__size ** 2
=======
#!/usr/bin/python3
"""Import the class"""
Rectangle = __import__('9-rectangle').Rectangle
"""
    Class Rectangle that inherits from BaseGeometry
"""


class Square(Rectangle):
    """
        My class
    """
    def __init__(self, size):
        """Constructor method"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
>>>>>>> 38492aa2f652bda047895a4871f5a072d0aa3090
