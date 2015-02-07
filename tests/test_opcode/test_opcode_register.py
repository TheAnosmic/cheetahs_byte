from unittest import TestCase

from opcode_ import OPCode, NOP, PRT, PrintOPCode


class TestOPCodeRegister(TestCase):
    def test_opcode_registered_nop(self):
        self.assertIn(NOP,
                      OPCode.get_all_opcodes())

    def test_opcode_register_print(self):
        self.assertIn(PRT,
                      OPCode.get_all_opcodes())

    def test_print_opcode_not_register_nop(self):
        self.assertNotIn(NOP,
                         PrintOPCode.get_all_opcodes())

    def test_print_opcode_register_print(self):
        self.assertIn(PRT,
                      PrintOPCode.get_all_opcodes())