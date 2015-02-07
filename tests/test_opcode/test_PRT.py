from unittest import TestCase

from opcode_ import PRT


class TestPRT(TestCase):
    def test_prt_code(self):
        op = PRT.build_from_string('\x10', None)
        exp = chr(PRT.CODE) + chr(0x10)
        self.assertEqual(op.build(), exp)

    def test_prt_name(self):
        self.assertEqual(PRT().NAME, 'PRT')