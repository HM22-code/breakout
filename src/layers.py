from enum import IntEnum, auto

class Layers(IntEnum):
    """ Layers class

    Args:
        IntEnum (_type_): layer level
    """
    BACKGROUND = auto()
    PLAYER = auto()
    UI = auto()