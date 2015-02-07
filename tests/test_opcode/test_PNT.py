from unittest import TestCase

from opcode_ import PNT


class TestPRT(TestCase):
    def test_pnt_code(self):
        op = PNT.build_from_string('\x10', None)
        exp = chr(PNT.CODE) + chr(~0x10 & 0xFF)
        self.assertEqual(op.build(), exp)
