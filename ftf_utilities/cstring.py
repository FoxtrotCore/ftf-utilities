from .color import *

class CString:
    """
    A wrapping class for python strings that have color attributes
    """
    def __init__(self, color, message):
        """
        self: Member function
        color: A Color enumeration (see ftfutils.Color)
        message: A message string
        """
        self.color = color
        self.message = message

    def __add__(self, other):
        """
        self: Member function
        other: Another CString object

        Returns a concatenation of two CStrings
        """
        return str(self) + str(other)

    def __radd__(self, other):
        """
        self: Member function
        other: Another CString object

        Returns a concatenation of two CStrings
        """
        return str(other) + str(self)

    def __repr__(self):
        """
        self: Member function

        Returns an ANSI formatted string
        """
        return Color.HEAD + self.color + self.message + str(Color.TAIL)

    def __str__(self):
        """
        self: Member function

        Returns an ANSI formatted string
        """
        return Color.HEAD + self.color + self.message + str(Color.TAIL)
