from primitive.byte import Byte
from opcode_.print_opcode import PrintOPCode


@PrintOPCode.register(0b00000001, 'PRT', 1 * 8)
class PRT(PrintOPCode):
    @classmethod
    def _build_from_string(cls, val, vm):
        return cls() + Byte(val)


@PrintOPCode.register(0b00000010, 'PNT', 1 * 8)
class PNT(PrintOPCode):
    @classmethod
    def _build_from_string(cls, val, vm):
        return cls() + Byte(~ord(val) & 0xFF)