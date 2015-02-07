import struct

from primitive import Primitive


class Int(Primitive):
    def __init__(self, val):
        super(Int, self).__init__()
        if isinstance(val, (int, long)) \
                and 0 <= val <= 0xFFFFFFFF:
            self.val = val
        else:
            raise ValueError("Must be int from 0-0xFFFFFFFF"
                             " not %r" % val)


    def get_size(self):
        return 32

    def build(self):
        return struct.pack('>I', self.val)

    def __str__(self):
        return '%X' % self.val

    def pprint(self):
        return '0x%X, %s' % (self.val, self.val)
