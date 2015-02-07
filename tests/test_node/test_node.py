from unittest import TestCase

from node import Node
from node.node_chain import NodeChain


class NodeTest(TestCase):
    def test_node_uuid(self):
        n = Node()
        n2 = Node()
        self.assertNotEqual(n.uuid, n2.uuid)

    def test_node_equals_by_uuid(self):
        n = Node()
        n2 = Node()
        n2.uuid = n.uuid
        self.assertEqual(n, n2)

    def test_node_in_list(self):
        n = Node()
        l = [1, 2, n]
        self.assertIn(n, l)

    def test_node_address_should_throw(self):
        n = Node()
        try:
            addr = n.address
        except AttributeError:
            pass
        else:
            self.fail("Should throw, got addr: %s" % addr)

    def test_node_address(self):
        n = Node()
        n.address = 0
        self.assertEqual(n.address, 0)

    def test_node_addition(self):
        n = Node()
        n2 = Node()
        nc = n + n2
        self.assertTrue(isinstance(nc, NodeChain))