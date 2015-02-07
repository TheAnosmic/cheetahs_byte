from unittest import TestCase

from opcode_ import JMP, PRT
from primitive import Int, Byte


class TestJumpOPCodes(TestCase):
    def test_fix_arg(self):
        pn = PRT()
        pn2 = PRT()
        jn = JMP(pn2)
        arg = Int(0)
        nc = pn + pn2 + jn + arg
        self.assertEqual(arg.build(), '\x00\x00\x00\x00')
        naddresses = {pn2.uuid: 8}
        ni = iter(nc)
        ni.next()  # pn
        ni.next()  # pn2
        ni.next()  # jn
        self.assertEqual(arg.build(), '\x00\x00\x00\x00')
        jn.fix_arg(naddresses, ni)
        self.assertEqual(arg.build(), Int(8).build())

    def test_fix_arg_raise_index_error(self):
        pn = PRT()
        jn = JMP(pn)
        nc = pn + jn
        naddresses = {pn.uuid: 8}
        ni = iter(nc)
        ni.next()  # pn
        ni.next()  # jn
        self.assertRaises(IndexError, jn.fix_arg, naddresses, ni)


    def test_fix_arg_raise_value_error_on_arg_size_mismatch(self):
        pn = PRT()
        jn = JMP(pn)
        bn = Byte(0)
        nc = pn + jn + bn
        naddresses = {pn.uuid: 8}
        ni = iter(nc)
        ni.next()  # pn
        ni.next()  # jn
        self.assertRaises(ValueError, jn.fix_arg, naddresses, ni)