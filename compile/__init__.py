from jmp_add import add_jmp_opcodes
from break_to_atoms import break_to_atoms
from linker import link_to_real_address
from compile import compile_from_string, build_to_bytecode
from opcode_pack import (ALLOWED_OPCODES, PRT_ONLY, PRT_AND_NOP,
                         PNT_PACK, JMP_PACK, REG_PACK, MEM_PACK)

from signature import SIGNATURE, test_signature