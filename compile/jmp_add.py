import random

from node import NodeChain
from opcode_ import JumpOPCodes
from primitive import get_primitive_class


def rechain_atom_chains(atoms,
                        chain_min=1,
                        chain_max=1):
    # TODO
    return atoms


def get_jmp_chain(jmp_opcode_classes, to_node):
    jmp_opcode_class = \
        random.choice(jmp_opcode_classes)
    jmp_opcode = jmp_opcode_class(to_node)
    primitive_class = \
        get_primitive_class(jmp_opcode.ARG_SIZE)
    return jmp_opcode + primitive_class(0)


def add_jmp_to_start(atoms, jmp_opcode_classes):
    first_node = atoms[0][0]
    nc = get_jmp_chain(jmp_opcode_classes, first_node)
    nc_atoms = [nc] + atoms
    return nc_atoms


def add_jmp_opcodes(atoms,
                    atom_min_size=1,
                    atom_max_size=1,
                    first_step_is_jmp=True,
                    jmp_opcode_classes=None):
    """
    Builds an atom list, with jumps connecting them.
    shuffle is allowed between nodes.
    although first step should remain first.
    :param atoms: target node chain
    :param atom_min_size: minimum size for each atom. not includes jmp.
    :param atom_max_size: maximum size for each atom. not includes jmp.
    :param first_step_is_jmp: add jump atom at the beginning
    :param jmp_opcode_classes: allowed jump opcodes, default to JumpOPCodes.get_all_opcodes
    :return: atom list.
    """
    jmp_opcode_classes = jmp_opcode_classes or \
                         JumpOPCodes.get_all_opcodes()

    atoms = rechain_atom_chains(atoms,
                                atom_min_size,
                                atom_max_size)
    for i in range(len(atoms) - 1):
        next_node = atoms[i + 1][0]
        jmp_nc = get_jmp_chain(
            jmp_opcode_classes, next_node)
        atoms[i].extend(jmp_nc)

    if first_step_is_jmp:
        atoms = add_jmp_to_start(atoms,
                                 jmp_opcode_classes)

    return atoms


def shuffle(atoms, keep_first=True):
    first = atoms[0]
    atoms = atoms[1:]
    random.shuffle(atoms)
    return [first] + atoms


def travel(atoms, current_atom):
    for node in current_atom:
        if isinstance(node, JumpOPCodes):
            jmp_node = node
            break
    else:
        return None

    target_uuid = jmp_node.target_uuid
    for atom in atoms:
        if target_uuid in atom:
            return atom

    raise IndexError("Target Atom: %s not in chain: %s." % (target_uuid, atoms))


def make_chain_from_atoms(atoms):
    return NodeChain(*[i for j in atoms for i in j])
