from byte import Byte
from int_ import Int


def get_primitive_class(size):
    if size == 8:
        return Byte
    elif size == 32:
        return Int
    raise ValueError("No Primitive for size: %s" % size)