from node import NodeChain
from opcode_ import OPCode


def node_to_atom(node, iterator):
    arg_size = node.get_arg_size()
    atom = NodeChain(node)

    while arg_size > 0:
        try:
            arg = iterator.next()
        except StopIteration:
            raise ValueError("Not enough arguments")
        if isinstance(arg, OPCode):
            raise ValueError("Currently not supporting"
                             " OPCode args")
        atom.append(arg)
        arg_size -= arg.get_size()

    if arg_size < 0:
        original_arg_size = node.get_arg_size()
        real_arg_size = original_arg_size + abs(arg_size)
        raise ValueError("Argument size mismatch,"
                         "Expecting: %s, Got %s"
                         "" % (original_arg_size, real_arg_size))

    return atom


def break_to_atoms(node_chain):
    i = iter(node_chain)
    atoms = NodeChain()

    for node in i:
        atoms.append(node_to_atom(node, i))

    return atoms
