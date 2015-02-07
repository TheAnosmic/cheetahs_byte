from uuid import UUID

from node import Node


class NodeChain(Node, list):
    def __init__(self, *args):
        Node.__init__(self)
        list.__init__(self, args)

    def get_size(self):
        return sum(n.get_size() for n in iter(self))

    def get_arg_size(self):
        return super(NodeChain, self).get_arg_size()

    def build(self):
        return ''.join(n.build() for n in iter(self))

    def append(self, p_object):
        super(NodeChain, self).append(p_object)
        return self

    def find(self, val):
        # TODO more pythonic
        # TODO Merge with __contains__
        if isinstance(val, UUID):
            for node in self:
                if node.uuid == val:
                    return node
            raise IndexError("UUID: %s not in chain" % val)
        elif isinstance(val, Node):
            for node in self:
                if node == val:
                    return node
            raise IndexError("Node: %s not in chain" % val)
        raise NotImplementedError(
            "Not supporting find for %s, %s"
            "" % (type(val), val))

    def __contains__(self, item):
        # TODO more pythonic
        if isinstance(item, UUID):
            for node in self:
                if node.uuid == item:
                    return node
            return False
        elif isinstance(item, Node):
            for node in self:
                if node == item:
                    return node
            return False
        raise NotImplementedError(
            "Not supporting find for %s, %s"
            "" % (type(item), item))


    def __add__(self, other):
        ret = self.copy()
        ret.append(other)
        return ret

    def __str__(self):
        return ' '.join(str(i) for i in self)


    def __repr__(self):
        return '<NC: %s>' % \
               ' '.join('%r' % i for i in self)

    def copy(self):
        return NodeChain(*self)