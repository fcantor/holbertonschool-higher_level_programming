#!/usr/bin/python3
'''
class Square module
'''
from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Square class which inherits from Rectangle class '''
    def __init__(self, size, x=0, y=0, id=None):
        ''' initialize Square class '''
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({:d}) {:d}/{:d} - {:d}"
                .format(self.id, self.x, self.y, self.width))
