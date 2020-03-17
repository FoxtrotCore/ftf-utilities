from enum import Enum

class Mode(Enum):
    """
    An enumeration for specifying message types (See ftf_utilities.utilities)
    """
    INFO = 0
    DEBUG = 1
    WARN = 2
    ERROR = 3
