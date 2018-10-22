#!/usr/bin/python3
'''
class Rectangle module
'''
from models.base import Base


class Rectangle(Base):
	''' Class Rectangle which inherits from Base class'''
	def __init__(self, width, height, x=0, y=0, id=None):
		''' Rectangle class initialization '''

		self.__width = width
		self.__height = height
		self.__x = x
		self.__y = y
		super().__init__(id)

		@property
		def width(self):
			''' width value getter '''
			return self.__width

		@width.setter
		def width(self, value):
			''' width value setter '''
			if type(value) is not int:
				raise TypeError("width must be an integer")
			if value <= 0:
				raise ValueError("width must be > 0")
			self.__width = width

		@property
		def height(self):
			''' height value getter '''
			return self._height

		@height.setter
		def height(self, height):
			''' height value setter '''
			if type(value) is not int:
				raise TypeError("height must be an integer")
			if value <= 0:
				raise ValueError("height must be > 0")
			self.__height = value

		@property
		def x(self):
			''' x value getter '''
			return self._x

		@x.setter
		def x(self, x):
			''' x value setter '''
			if type(value) is not int:
				raise TypeError("x must be an integer")
			if value < 0:
				raise ValueError("x must be >= 0")
			self.__x = value

		@property
		def y(self):
			''' y value getter '''
			return self._y

		@y.setter
		def y(self, y):
			''' y value setter '''
			if type(value) is not int:
				raise TypeError("y must be an integer")
			if value < 0:
				raise ValueError("y must be >= 0")
			self.__y = value