from node import NodeChain
from opcode_ import OPCode, PrintOPCode
from primitive import Byte


class RegisterOPCode(OPCode):
    _all_opcodes = []
    pass


@RegisterOPCode.register(0b00100000, "RAD", arg_size=8)
class RAD(RegisterOPCode):
    pass


@RegisterOPCode.register(0b00100001, "RSB", arg_size=8)
class RSB(RegisterOPCode):
    pass


@RegisterOPCode.register(0b00000100, "PRR", arg_size=0)
class PRR(RegisterOPCode, PrintOPCode):
    ARG_IN_BYTECODE = False

    @classmethod
    def _build_from_string(cls, s, vm):
        val = ord(s)
        change = val - vm.register
        if change:
            vm.register += change
            if change > 0:
                op = RAD
            else:
                op = RSB
            return op() + Byte(abs(change)) + cls()
        return NodeChain(cls())
