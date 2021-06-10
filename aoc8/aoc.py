input = '''
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6
'''

# parse each code
# pair with index

code = input.strip().split('\n')

opCodeIdx = tuple((i, tuple(op.split())) for i, op in enumerate(code))


class OpCode:

	previousOps = {}

	def __init__(self) -> None:
	    codeIdx = 0

	