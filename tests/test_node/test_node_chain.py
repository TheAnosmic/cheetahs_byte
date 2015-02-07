from unittest import TestCase
from uuid import uuid4

from opcode_ import PRT
from primitive.byte import Byte
from node import Node
from node.node_chain import NodeChain


class TestNodeChain(TestCase):
    def test_create_from_nothing(self):
        nc = NodeChain()
        self.assertFalse(nc)

    def test_create_from_two_nodes(self):
        n = Node()
        n2 = Node()
        nc = NodeChain(n, n2)
        self.assertEqual(n, nc[0])
        self.assertEqual(n2, nc[1])

    def test_build(self):
        n = Byte(0x10)
        n2 = Byte(0x20)
        nc = n + n2
        self.assertEqual(nc.build(), '\x10\x20')

    def test_add_node_chain(self):
        n = PRT()
        n2 = Byte(0x20)
        nc = n + n2
        n3 = Byte(0x10)
        n4 = Byte(0x20)
        nc2 = n3 + n4
        nc3 = nc + nc2
        self.assertIsInstance(nc3, NodeChain)
        self.assertIsInstance(nc3[0], Node)
        self.assertNotIsInstance(nc3[0], NodeChain)

    def test_copy(self):
        n = Byte(0xFF)
        n2 = PRT()
        nc = n + n2
        nc2 = nc.copy()
        nc2.append(Byte(0x30))
        self.assertEqual(len(nc), 2)
        self.assertEqual(len(nc2), 3)

    def test_find_uuid(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        found = nc.find(byte.uuid)
        self.assertEqual(found, byte)

    def test_find_node(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        found = nc.find(byte)
        self.assertEqual(found, byte)

    def test_not_found_uuid(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        self.assertRaises(IndexError, nc.find, uuid4())

    def test_not_found_node(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        self.assertRaises(IndexError, nc.find, PRT())


    def test_find_not_supported_type(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        self.assertRaises(NotImplementedError, nc.find, 'TheAnosmic')


    def test_contains_uuid(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        self.assertIn(byte, nc)

    def test_contains_node(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        self.assertIn(byte, nc)

    def test_not_contains_uuid(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        self.assertNotIn(uuid4(), nc)

    def test_not_contains_node(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        self.assertNotIn(PRT(), nc)

    def test_contains_not_supported_type(self):
        byte = Byte(0x40)
        nc = PRT() + byte
        self.assertRaises(NotImplementedError, nc.__contains__, 'TheAnosmic')