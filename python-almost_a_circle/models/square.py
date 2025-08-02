#!/usr/bin/python3
""" Square class """

from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        attrs = ['id', 'size', 'x', 'y']
        if args and len(args) > 0:
            for i, value in enumerate(args):
                if attrs[i] == 'size':
                    self.size = value
                else:
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                if key == 'size':
                    self.size = value
                else:
                    setattr(self, key, value)

    def to_dictionary(self):
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
