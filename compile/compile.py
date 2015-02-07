import random

from break_to_atoms import break_to_atoms
from jmp_add import add_jmp_opcodes, shuffle, make_chain_from_atoms
from node import NodeChain
from opcode_.jmp_opcodes import JumpOPCodes
from opcode_.print_opcode import PrintOPCode
from vm import VM
from opcode_ import OPCode, HLT, NOP
from linker import link_to_real_address


def string_to_prt_opcodes(string, print_opcodes, vm):
    if not print_opcodes:
        raise ValueError("Can't without print opcodes")
    opcodes = NodeChain()
    for c in string:
        opcode = random.choice(print_opcodes)
        opcodes.extend(opcode.build_from_string(c, vm))
    return opcodes


def add_random_nops(atoms):
    for i in range(len(atoms)):
        if not random.randint(0, 10):
            atoms.insert(i, NodeChain(NOP()))


def compile_from_string(string,
                        allowed_opcodes=None):
    """
    :param allowed_opcodes: from opcode_pack
    """
    allowed_opcodes = allowed_opcodes or \
                      OPCode.get_all_opcodes()
    vm = VM()
    print_opcodes = filter(lambda op:
                           issubclass(op, PrintOPCode),
                           allowed_opcodes)
    jump_opcodes = filter(lambda op:
                          issubclass(op, JumpOPCodes),
                          allowed_opcodes)
    nc = string_to_prt_opcodes(string, print_opcodes, vm)
    atoms = break_to_atoms(nc)
    if NOP in allowed_opcodes:
        add_random_nops(atoms)
    atoms.append(NodeChain(HLT()))
    if jump_opcodes:
        atoms = add_jmp_opcodes(atoms, jmp_opcode_classes=jump_opcodes)
        atoms = shuffle(atoms)
    nc = make_chain_from_atoms(atoms)
    link_to_real_address(nc)
    return nc

