from primitive import Primitive


class Byte(Primitive):
    def __init__(self, val):
        super(Byte, self).__init__()
        if isinstance(val, int) and 0 <= val <= 255:
            self.val = chr(val)
        elif isinstance(val, str) and len(val) == 1:
            self.val = val
        else:
            raise ValueError("Must be int from 0-255"
                             " or len 1 str, not"
                             " %r" % val)

    def build(self):
        return self.val

    def get_size(self):
        return 8

    def __str__(self):
        return '%X' % ord(self.val)

    def pprint(self):
        return '0x%X, %s' % (ord(self.val), self.val)