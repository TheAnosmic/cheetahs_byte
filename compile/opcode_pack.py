"""
Choose the complexity of the bytecode generated.

"""
from opcode_ import PRT, PNT, HLT, NOP, JMP, RAD, RSB, PRR, MAC, MSM, MSC, MAM, PRM

PRT_ONLY = [PRT, HLT]
PRT_AND_NOP = PRT_ONLY + [NOP]
PNT_PACK = PRT_ONLY + [PNT]

JMP_PACK = PRT_AND_NOP + [JMP]

REG_PACK = JMP_PACK + [RAD, RSB, PRR]

MEM_PACK = REG_PACK + [MAC, MSM, MSC, MAM, PRM]

ALLOWED_OPCODES = {
    1: PRT_ONLY,
    'EASIEST': PRT_ONLY,
    2: PRT_AND_NOP,
    3: PNT_PACK,
    4: JMP_PACK,
    5: REG_PACK,
    6: MEM_PACK,
    'HARDEST': MEM_PACK,
}