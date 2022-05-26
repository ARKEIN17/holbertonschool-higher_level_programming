#!/usr/bin/python3

"""Create a empty class"""


class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size
    '''Definitios'''
    @size.setter
    def size(self, value):
        '''Validations'''
        if type(value) != int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        a = self.__size * self.__size
        '''Returns'''
        return a
