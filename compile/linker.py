# Not a real linker, but that name describes is best
from opcode_ import JumpOPCodes


def get_node_addresses(node_chain):
    node_addresses = {}
    current_address = 0

    for node in node_chain:
        node_addresses[node.uuid] = current_address
        node.address = current_address
        current_address += node.get_size()

    return node_addresses


def link_to_real_address(node_chain):
    node_addresses = get_node_addresses(node_chain)
    i = iter(node_chain)
    for node in i:
        if isinstance(node, JumpOPCodes):
            node.fix_arg(node_addresses, i)
