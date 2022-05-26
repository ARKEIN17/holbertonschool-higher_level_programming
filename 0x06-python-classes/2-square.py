#!/usr/bin/python3

'''the Square Class'''


class Square:
    '''Definitions'''
    def __init__(self, size=0):
        '''type error int'''
        if type(size) is not int:
            raise TypeError('size must be an integer')
            '''Less than 0'''
        elif size < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = size
