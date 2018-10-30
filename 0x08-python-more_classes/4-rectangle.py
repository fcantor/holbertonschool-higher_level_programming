#!/usr/bin/python3
'''
Rectangle class definition
'''


class Rectangle():
    '''
    Rectangle class with width and height getter/setter methods
    '''

    def __init__(self, width=0, height=0):
        ''' initializes the rectangle class '''
        self.width = width
        self.height = height

    @property
    def width(self):
        ''' width value getter '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' width value setter '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        ''' height value getter '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' height value setter '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        ''' calculates the area of the rectangle '''
        return self.height * self.width

    def perimeter(self):
        ''' calculates the perimeter of the rectangle '''
        if self.width is 0 or self.height is 0:
            return 0
        else:
            return (2 * self.height) + (2 * self.width)

    def __str__(self):
        ''' prints the rectangle '''
        if self.area() == 0:
            return ""
        return '\n'.join(['#' * self.width] * self.height)

    def __repr__(self):
        ''' returns a string representation of the rectangle '''
        return ("Rectangle({}, {})".format(self.width, self.height))
