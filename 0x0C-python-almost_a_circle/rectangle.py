#!/usr/bin/python3
"""0x0C. Python - Almost a circle, task 2 - 13"""
from models.base import Base


class Rectangle(Base):
    """Creates rectangle objects with 2 dimensions and offset coordinates.
    Uses superclass `__init__` to create valid instance id, and sets
    self vars from args.
    Args:
        width (int): x dimension of rectangle
        height (int): y dimension of rectangle
        x (int): horizontal offset of rectangle
        y (int): vertical offset of rectangle
        id (int): unique identifer for each instance of super()
    Project task:
        2. First Rectangle - __init__, getters and setters for `width`,
            `height`, `x`, `y`
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        # attribute assigment here engages setters defined below
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __integer_validator(self, attr, value):
        """Validates incoming argument values for use with internal attributes.
        Args:
            attr (str): name of intended attribute assignment
            value (any): expecting int, but will filter out other types
        Raises:
            TypeError: if any incoming value is not (int)
            ValueError: if any `width` or `height` candidate is <= 0, or if
                `x` or `y` candidates are < 0
        Project task:
            3. Validate attributes - input validation for `width`, `height`,
                `x`, `y`
        """
        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(attr))
        if attr is 'width' or attr is 'height':
            if value <= 0:
                raise ValueError('{} must be > 0'.format(attr))
        elif attr is 'x' or attr is 'y':
            if value < 0:
                raise ValueError('{} must be >= 0'.format(attr))

    @property
    def width(self):
        """`__width` getter
        Returns:
            __width (int): x dimension of rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """Args:
            value (int): x dimension of rectangle
        Attributes:
            __width (int): x dimension of rectangle
        """
        self.__integer_validator('width', value)
        self.__width = value

    @property
    def height(self):
        """`__height` getter
        Returns:
            __height (int): y dimension of rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """Args:
            value (int): y dimension of rectangle
        Attributes:
            __height (int): y dimension of rectangle
        """
        self.__integer_validator('height', value)
        self.__height = value

    @property
    def x(self):
        """`__x` getter
        Returns:
            __x (int): horizontal offset of rectangle
        """
        return self.__x

    @x.setter
    def x(self, value):
        """Args:
            value (int): horizontal offset of rectangle
        Attributes:
            __x (int): horizontal offset of rectangle
        """
        self.__integer_validator('x', value)
        self.__x = value

    @property
    def y(self):
        """`__y` getter
        Returns:
            __y (int): vertical offset of rectangle
        """
        return self.__y

    @y.setter
    def y(self, value):
        """Args:
            value (int): vertical offset of rectangle
        Attributes:
            __y (int): vertical offset of rectangle
        """
        self.__integer_validator('y', value)
        self.__y = value

    def area(self):
        """Returns area of rectangle as product of `width` and `height`.
        Returns:
            `__width` * `__height`
        Project tasks:
            4. Area first - public method `area()`
        """
        return self.width * self.height

