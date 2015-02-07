from unittest import TestCase

from opcode_ import PRT, JMP
from compile import link_to_real_address
from primitive import Int


class TestLinker(TestCase):
    def test_linker_address(self):
        pn = PRT()
        pn2 = PRT()
        pn3 = PRT()
        nc = pn + pn2 + pn3
        self.assertRaises(
            AttributeError, getattr, pn, 'address')
        link_to_real_address(nc)
        self.assertEqual(pn.address, 0)
        self.assertEqual(pn2.address, 8)
        self.assertEqual(pn3.address, 16)


    def test_linker_jmp(self):
        pn = PRT()
        jn = JMP(pn)
        i = Int(0)
        nc = pn + jn + i
        self.assertRaises(
            AttributeError, getattr, jn, 'address')
        self.assertRaises(
            AttributeError, getattr, jn, 'other_node_address')
        link_to_real_address(nc)
        self.assertEqual(0, jn.other_node_address)

    def test_linker_jmp_reverse_order(self):
        pn = PRT()
        jn = JMP(pn)
        nc = jn + Int(0) + pn
        self.assertRaises(
            AttributeError, getattr, jn, 'address')
        self.assertRaises(
            AttributeError, getattr, jn, 'other_node_address')
        link_to_real_address(nc)
        self.assertEqual(40, jn.other_node_address)