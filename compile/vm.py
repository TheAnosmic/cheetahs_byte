from collections import deque
from signature import SIGNATURE, test_signature

MEMORY_SIZE = 256


class VM(object):
    def __init__(self):
        self.register = 0
        self.memory = [0] * MEMORY_SIZE


class RunnerVM(VM):
    def __init__(self, bytecode, signature=SIGNATURE):
        super(RunnerVM, self).__init__()
        test_signature(bytecode, signature)
        bytecode = bytecode[len(signature):]
        self.pc = 0
        self.bytecode = bytecode
        self.halt = False
        self.out = ''
        self.opcode_used = set()
        self.last_execute = deque(maxlen=16)