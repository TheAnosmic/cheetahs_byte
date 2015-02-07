from node import Node


class OPCode(Node):
    # if two underscores it makes problems with register
    _all_opcodes = []

    CODE = 0b00000000
    NAME = 'INV'
    ARG_SIZE = 0

    def __init__(self):
        super(OPCode, self).__init__()

    def get_size(self):
        return 8

    def get_arg_size(self):
        return self.ARG_SIZE

    def build(self):
        return chr(self.CODE)

    @classmethod
    def get_all_opcodes(cls):
        return cls._all_opcodes

    @classmethod
    def register(cls, code, name, arg_size=0):
        def _register(klass):
            klass.CODE = code
            klass.NAME = name
            klass.ARG_SIZE = arg_size
            cls._all_opcodes.append(klass)
            for parent in cls.__bases__:
                if hasattr(parent, 'register'):
                    parent.register(code, name, arg_size)(klass)
            return klass

        return _register

    def __str__(self):
        return self.NAME

    @staticmethod
    def get_opcode_for_code(code):
        for opcode in OPCode.get_all_opcodes():
            if opcode.CODE == code:
                return opcode