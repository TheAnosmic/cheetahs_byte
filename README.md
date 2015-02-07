# cheetahs_byte

As an exercise for students who just learned pointers in C++,
we gave an assignment to write a simple bytecode executor.

This is the instructor side, which can create the bytecode,
according to the level of the specific student,
and according to the result that should be printed out after a successful run.

How to use:
    opcode_pack = MEM_PACK
    node_chain = compile_from_string("Hello", allowed_opcodes=opcode_pack)
    bytecode = node_chain.build()
    
usage sample is also at the file run.py.

most of the code is tested,
some code is not the most beautiful i've written,
the problem is i continued the writing at work,
and i can't post code that was written there.
