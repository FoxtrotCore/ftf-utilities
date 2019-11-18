class Color(Enum):
    HEAD = '\033['

    BLACK = '30m'
    RED = '31m'
    GREEN = '32m'
    YELLOW = '33m'
    BLUE = '34m'
    MAGENTA = '35m'
    CYAN = '36m'
    WHITE = '37m'
    GRAY = '90m'

    B_RED = '91m'
    B_GREEN = '92m'
    B_YELLOW = '93m'
    B_BLUE = '94m'
    B_MAGENTA = '95m'
    B_CYAN = '96m'
    B_WHITE = '97m'

    TAIL = '\033[0m'

    def __add__(self, other):
        if(other is Color): return self.value + other.value
        else: return self.value + str(other)
    def __radd__(self, other): return str(self) + str(other)
    def __repr__(self): return str(self.value)
    def __str__(self):  return str(self.value)
