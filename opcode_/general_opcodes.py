from opcode_ import OPCode


class GeneralOPCode(OPCode):
    _all_opcodes = []


@GeneralOPCode.register(0b11111110, 'NOP')
class NOP(GeneralOPCode):
    pass


@GeneralOPCode.register(0b11111111, 'HLT')
class HLT(GeneralOPCode):
    pass