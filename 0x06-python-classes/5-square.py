#!/usr/bin/python3

'''Init of the program'''


class Square:
    """square with size"""
    def __init__(self, size=0):
        """adding value to size atribute"""
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        '''Validations'''
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """area of the operation"""
        a = self.__size * self.__size
        return a

    def my_print(self):
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end="")
            print()
