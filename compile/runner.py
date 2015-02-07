import struct

from vm import RunnerVM
from opcode_ import PRT, NOP, PNT, JMP, OPCode, HLT, RAD, PRR, RSB, MAC, PRM, MAM, MSC, MSM


def set_vm_pc(vm, val):
    vm.pc = val


def set_halt(vm):
    vm.halt = True


def h_PRT(vm):
    vm.out += (vm.bytecode[vm.pc])
    vm.pc += 1
    vm.last_execute.append('PRT: %r' % vm.bytecode[vm.pc])


def h_PNT(vm):
    s = chr(~ord(vm.bytecode[vm.pc]) & 0xFF)
    vm.out += (s)
    vm.pc += 1
    vm.last_execute.append('PRT: %r' % s)


def h_JMP(vm):
    pc = vm.pc
    i = vm.bytecode[pc:pc + 4]
    pc = struct.unpack('>I', i)[0] / 8
    vm.pc = pc
    vm.last_execute.append('JMP: %r' % i)


def h_RAD(vm):
    vm.register += ord(vm.bytecode[vm.pc])
    vm.pc += 1
    vm.last_execute.append('RAD: %r' % vm.bytecode[vm.pc])


def h_RSB(vm):
    vm.register -= ord(vm.bytecode[vm.pc])
    vm.pc += 1
    vm.last_execute.append('RSB: %r' % vm.bytecode[vm.pc])


def h_PRR(vm):
    vm.out += chr(vm.register)
    vm.last_execute.append('PRR: %r' % vm.register)


def h_MAC(vm):
    arg1 = vm.bytecode[vm.pc]
    vm.pc += 1
    arg2 = vm.bytecode[vm.pc]
    vm.pc += 1
    arg1 = ord(arg1)
    arg2 = ord(arg2)
    vm.last_execute.append('MAC: %s:%r += %r'
                           '' % (arg1, vm.memory[arg1], arg2))
    vm.memory[arg1] += arg2


def h_MSC(vm):
    arg1 = vm.bytecode[vm.pc]
    vm.pc += 1
    arg2 = vm.bytecode[vm.pc]
    vm.pc += 1
    arg1 = ord(arg1)
    arg2 = ord(arg2)
    vm.last_execute.append('MSC: %s:%r -= %r'
                           '' % (arg1, vm.memory[arg1], arg2))
    vm.memory[arg1] -= arg2


def h_MAM(vm):
    arg1 = vm.bytecode[vm.pc]
    vm.pc += 1
    arg2 = vm.bytecode[vm.pc]
    vm.pc += 1
    arg1 = ord(arg1)
    arg2 = ord(arg2)

    vm.last_execute.append('MAM: %s:%r += %s:%r' % (
        arg1, vm.memory[arg1], arg2, vm.memory[arg2]))
    vm.memory[arg1] += vm.memory[arg2]


def h_MSM(vm):
    arg1 = vm.bytecode[vm.pc]
    vm.pc += 1
    arg2 = vm.bytecode[vm.pc]
    vm.pc += 1
    arg1 = ord(arg1)
    arg2 = ord(arg2)

    vm.last_execute.append('MSM: %s:%r -= %s:%r' % (
        arg1, vm.memory[arg1], arg2, vm.memory[arg2]))
    vm.memory[arg1] -= vm.memory[arg2]


def h_PRM(vm):
    arg1 = vm.bytecode[vm.pc]
    vm.pc += 1
    vm.last_execute.append('PRM: %r' % (ord(arg1), ))
    vm.out += chr(vm.memory[ord(arg1)])


handlers = {
    NOP: lambda vm: True,
    PRT: h_PRT,
    PNT: h_PNT,
    JMP: h_JMP,
    RAD: h_RAD,
    RSB: h_RSB,
    PRR: h_PRR,
    MAC: h_MAC,
    MSC: h_MSC,
    MAM: h_MAM,
    MSM: h_MSM,
    PRM: h_PRM,
    HLT: lambda vm: set_halt(vm)
}


def run(bytecode, runner_vm):
    runner_vm = runner_vm or RunnerVM(bytecode)
    runner_vm.pc = 0
    runner_vm.halt = False
    runner_vm.out = ''
    runner_vm.opcode_used = set()
    try:
        while not runner_vm.halt:
            opcode = bytecode[runner_vm.pc]
            opcode = OPCode.get_opcode_for_code(ord(opcode))
            runner_vm.opcode_used.add(opcode)
            runner_vm.pc += 1
            handlers[opcode](runner_vm)
    except Exception:
        print '\n'.join(runner_vm.last_execute)
        raise
