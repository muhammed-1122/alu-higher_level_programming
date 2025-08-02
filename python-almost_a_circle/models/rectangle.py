#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # width
    @property
    def width(self): return self.__width
    @width.setter
    def width(self, value):
        if type(value) != int: raise TypeError("width must be an integer")
        if value <= 0: raise ValueError("width must be > 0")
        self.__width = value

    # height
    @property
    def height(self): return self.__height
    @height.setter
    def height(self, value):
        if type(value) != int: raise TypeError("height must be an integer")
        if value <= 0: raise ValueError("height must be > 0")
        self.__height = value

    # x
    @property
    def x(self): return self.__x
    @x.setter
    def x(self, value):
        if type(value) != int: raise TypeError("x must be an integer")
        if value < 0: raise ValueError("x must be >= 0")
        self.__x = value

    # y
    @property
    def y(self): return self.__y
    @y.setter
    def y(self, value):
        if type(value) != int: raise TypeError("y must be an integer")
        if value < 0: raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.width * self.height

    def display(self):
        print("\n" * self.y, end='')
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        attrs = ['id', 'width', 'height', 'x', 'y']
        if args and len(args) > 0:
            for i, val in enumerate(args):
                setattr(self, attrs[i], val)
        else:
            for k, v in kwargs.items():
                if k in attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }
