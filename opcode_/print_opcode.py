from opcode_.opcode import OPCode


class PrintOPCode(OPCode):
    _all_opcodes = []
    ARG_IN_BYTECODE = True

    @classmethod
    def _build_from_string(cls, s, vm):
        raise NotImplementedError(
            "PrintOPCode is an interface, probably ment PRT")

    @classmethod
    def build_from_string(cls, s, vm):
        if not isinstance(s, str):
            raise ValueError(
                "Must be string (not even unicode for now)")

        if cls.ARG_IN_BYTECODE:
            if len(s) * 8 != cls.ARG_SIZE:
                raise ValueError("String length: %s, "
                                 "needs to be: %s"
                                 "" % (len(s), cls.ARG_SIZE / 8))

        return cls._build_from_string(s, vm)



