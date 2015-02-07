from uuid import uuid4 as uuid


class Node(object):
    def __init__(self):
        self.uuid = uuid()
        self.__address = None
        self.friendly_uuid = ('%s' % self.uuid)[-5:]

    def build(self):
        raise NotImplementedError("Abstract Node")

    def get_size(self):
        raise NotImplementedError("Abstract Node")

    def get_arg_size(self):
        return 0

    @property
    def address(self):
        if self.__address is None:
            raise AttributeError('Address not supplied')
        return self.__address

    @address.setter
    def address(self, address):
        self.__address = address

    def has_address(self):
        return self.__address is not None

    def __repr__(self):
        identifier = self.friendly_uuid if not self.has_address() else self.address
        return '<NOD %s>' % identifier

    def __str__(self):
        return 'NOD'

    def __add__(self, other):
        return NodeChain(self, other)

    def __hash__(self):
        return self.uuid

    def __eq__(self, other):
        if not isinstance(other, Node):
            return NotImplemented
        return self.uuid == other.uuid


# circular
from node_chain import NodeChain