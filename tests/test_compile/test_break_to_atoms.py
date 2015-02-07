from unittest import TestCase

from compile.break_to_atoms import break_to_atoms
from opcode_ import PRT
from opcode_ import JMP
from primitive import Int, Byte


class TestJMPShuffle(TestCase):
    def test_break_to_one(self):
        nc = PRT.build_from_string('t', None)
        broken = break_to_atoms(nc)
        self.assertEqual(len(broken), 1)

    def test_break_to_two(self):
        nc = PRT.build_from_string('t', None)
        nc2 = PRT.build_from_string('q', None)
        nc.extend(nc2)
        broken = break_to_atoms(nc)
        self.assertEqual(len(broken), 2)

    def test_break_to_one_int(self):
        nc = JMP(PRT()) + Int(0xFFFFFFFF)
        broken = break_to_atoms(nc)
        self.assertEqual(len(broken), 1)

    def test_break_to_one_and_one_byte(self):
        prt = PRT()
        nc = JMP(prt) + Int(100) + prt + Byte(255)
        broken = break_to_atoms(nc)
        self.assertEqual(len(broken), 2)

    def test_break_to_one_with_too_small_arg_size(self):
        nc = JMP(PRT()) + Byte(100)
        self.assertRaises(ValueError, break_to_atoms, nc)

    def test_break_to_one_with_too_big_arg_size(self):
        nc = PRT() + Int(100)
        self.assertRaises(ValueError, break_to_atoms, nc)