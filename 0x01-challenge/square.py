#!/usr/bin/python3
'''A square class'''


class square():
    """
    A square class
    Attributes:
    width = 0
    height = 0
    """

    def __init__(self, width=0, height=0):
        '''Define the square initials'''
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Define the Area of the square """
        return self.width * self.width

    def PermiterOfMySquare(self):
        '''Define the perimeter of the square'''
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        '''Define the string of the square'''
        return "{}/{}".format(self.width, self.height)

    if __name__ == "__main__":
        s = square(width=12, height=9)
        print(s)
        print(s.area_of_my_square())
        print(s.PermiterOfMySquare())
