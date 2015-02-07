
SIGNATURE = 'CheetahsByte'

def test_signature(bytecode, signature=SIGNATURE):
    if not bytecode.startswith(signature):
        raise ValueError("Signature mismatch")