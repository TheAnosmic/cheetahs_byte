# TODO: Add format
from primitive import Primitive


def disassemble(node_chain):
    ret = []
    address = 0
    fmt = '%8X: %s'
    for i in node_chain:
        if isinstance(i, Primitive):
            s = i.pprint()
        else:
            s = str(i)
        ret.append(fmt % (address, s))
        address += i.get_size()

    return ret