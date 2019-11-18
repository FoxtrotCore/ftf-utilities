from ftfutils.color import *

class CString:
    def __init__(self, color, message):
        self.color = color
        self.message = message

    def __add__(self, other): return str(self) + str(other)
    def __radd__(self, other): return str(other) + str(self)
    def __repr__(self): return Color.HEAD + self.color + self.message + str(Color.TAIL)
    def __str__(self):  return Color.HEAD + self.color + self.message + str(Color.TAIL)
