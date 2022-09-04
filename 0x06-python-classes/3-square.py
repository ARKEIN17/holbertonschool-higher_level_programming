#!/usr/bin/python3

'''Init of the program'''


class Square:
    '''Definitios'''
    def __init__(self, size=0):
        '''Validations'''
        if type(size) != int:
            raise TypeError('size must be an integer')
            '''Less than 0'''
        elif size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        '''Returns'''
        are = self.__size * self.__size
        return are
