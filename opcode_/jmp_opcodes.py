from opcode_ import OPCode


class JumpOPCodes(OPCode):
    _all_opcodes = []

    def __init__(self, other_node):
        super(JumpOPCodes, self).__init__()
        self.target_uuid = other_node.uuid
        self.__target_address = None

    @property
    def other_node_address(self):
        if self.__target_address is None:
            raise AttributeError("No Address set")
        return self.__target_address

    @other_node_address.setter
    def other_node_address(self, value):
        self.__target_address = value

    def fix_arg(self, node_addresses, node_iterator):
        other_not_uuid = self.target_uuid
        other_node_address = node_addresses.get(
            other_not_uuid, None)

        if other_node_address is None:
            raise IndexError("No node with UUID: %s in chain"
                             "" % other_not_uuid)
        self.other_node_address = other_node_address
        try:
            arg = node_iterator.next()
        except StopIteration:
            raise IndexError("JMP has no arg")
        if arg.get_size() != self.get_arg_size():
            raise ValueError("Arg size mismatch: Need %s,"
                             " Found %s" % (
                                 self.get_arg_size(), arg.get_size()))
        arg.val = other_node_address


@JumpOPCodes.register(0b00010000, 'JMP', 32)
class JMP(JumpOPCodes):
    pass