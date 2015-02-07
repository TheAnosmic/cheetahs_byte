# from some point i had no time to make real unittests
# i had to test blackbox... );

from unittest import TestCase

from compile.compile import compile_from_string
from compile.opcode_pack import ALLOWED_OPCODES
from compile.runner import run
from compile.vm import RunnerVM


class TestBlackBox(TestCase):
    def test_opcode_used1(self):
        for allowed_opcodes in ALLOWED_OPCODES.values():
            bc = compile_from_string('S' * 200, allowed_opcodes)
            bc = bc.build()
            vm = RunnerVM(bc)
            run(bc, vm)
            self.assertTrue(vm.opcode_used.issubset(allowed_opcodes))

    def test_output(self):
        output = ''.join(chr(i) for i in range(255)) * 10
        bc = compile_from_string(output)
        bc = bc.build()
        vm = RunnerVM(bc)
        run(bc, vm)
        self.assertEqual(vm.out, output)
