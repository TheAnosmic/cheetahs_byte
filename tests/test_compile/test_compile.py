from unittest import TestCase

from compile.compile import string_to_prt_opcodes
from compile.vm import VM
from opcode_ import PRT


class TestCompile(TestCase):
    def test_string_to_prt_opcodes(self):
        s = '1337'
        nc = string_to_prt_opcodes(s, [PRT], VM())
        self.assertIsInstance(nc[0], PRT)
        self.assertEqual(nc[1].val, '1')
        self.assertIsInstance(nc[2], PRT)
        self.assertEqual(nc[3].val, '3')
        self.assertIsInstance(nc[4], PRT)
        self.assertEqual(nc[5].val, '3')
        self.assertIsInstance(nc[6], PRT)
        self.assertEqual(nc[7].val, '7')


