from random import random, randint

from node.node_chain import NodeChain
from opcode_ import OPCode, PrintOPCode
from primitive import Byte
from compile.vm import MEMORY_SIZE


class MemOPCodes(OPCode):
    _all_opcodes = []


@MemOPCodes.register(0b01000000, "MAC", 16)
class MAC(MemOPCodes):
    pass


@MemOPCodes.register(0b01000001, "MSC", 16)
class MSC(MemOPCodes):
    pass


@MemOPCodes.register(0b01000010, "MAM", 16)
class MAM(MemOPCodes):
    pass


@MemOPCodes.register(0b01000011, "MSM", 16)
class MSM(MemOPCodes):
    pass


@MemOPCodes.register(0b00001000, "PRM", arg_size=8)
class PRM(MemOPCodes, PrintOPCode):
    @staticmethod
    def __change_mem_loc_to_val(vm, mem_loc, dst_val):
        current_val = vm.memory[mem_loc]
        change = dst_val - current_val
        vm.memory[mem_loc] += change
        op = MAC if change > 0 else MSC
        mem_loc_byte = Byte(mem_loc)
        change_byte = Byte(abs(change))
        return op() + mem_loc_byte + change_byte

    @classmethod
    def _build_from_string(cls, s, vm):
        # Warning: this code was written past my bed time.
        dst_val = ord(s)
        mem_loc = randint(0, MEMORY_SIZE - 1)
        mem_loc_val = vm.memory[mem_loc]
        change = dst_val - mem_loc_val

        if not change:
            return PRM() + Byte(mem_loc)

        from_const = random() >= 0.5

        if from_const:
            chain = PRM.__change_mem_loc_to_val(vm, mem_loc, dst_val)

        else:
            other_mem_loc = randint(0, MEMORY_SIZE - 1)
            while other_mem_loc == mem_loc:
                other_mem_loc = randint(0, MEMORY_SIZE - 1)  # random fun
            other_mem_loc_val = vm.memory[other_mem_loc]
            if other_mem_loc_val != change:
                chain = PRM.__change_mem_loc_to_val(vm, other_mem_loc, abs(change))
            else:
                chain = NodeChain()
            op = MAM if change > 0 else MSM
            vm.memory[mem_loc] += change
            chain.extend(op() + Byte(mem_loc) + Byte(other_mem_loc))

        chain.extend(PRM() + Byte(mem_loc))
        return chain
