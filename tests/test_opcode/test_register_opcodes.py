# Again, sorry for black box testing, no time.

from unittest import TestCase

from compile.vm import VM
from opcode_ import PRR, RAD, RSB


class TestRegisterOPCodes(TestCase):
    def test_build1(self):
        vm = VM()
        PRR.build_from_string('a', vm)
        self.assertEqual(vm.register, ord('a'))
        s = PRR.build_from_string('b', vm)
        self.assertIsInstance(s[0], RAD)
        self.assertEqual(vm.register, ord('b'))
        self.assertEqual(s[1].val, chr(1))
        s = PRR.build_from_string('a', vm)
        self.assertIsInstance(s[0], RSB)
        self.assertEqual(s[1].val, chr(1))
