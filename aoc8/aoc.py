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
# write execute op code func, check previous code,

with open('input.txt', 'r') as f:
	my_input = f.readlines()

myInput = tuple(map(lambda x: tuple(x.split()), my_input))

print(myInput)


# code = input.strip().split('\n')

# opCodeIdx = tuple(tuple(op.split()) for op in code)
# print(opCodeIdx)


class OpCode:


	previousOps = set()
	acc = 0

	def __init__(self, codeInput):
	  self.codeInput = codeInput
	  self.codeIdx = 0
	  self.currentCode = self.codeInput[self.codeIdx]
	  self.loopComplete = False

	def execute(self):
		print(f"index: {self.codeIdx} Current Code: {self.currentCode}")
		print(self.previousOps)
		print("Accumulator: ", self.acc)
		if self.codeIdx in self.previousOps:
			self.loopComplete = True
			return
		else:
			self.previousOps.add(self.codeIdx)
		
		if self.currentCode[0] == 'nop':
			self.codeIdx += 1
			self.currentCode = self.codeInput[self.codeIdx]
			return
		elif self.currentCode[0] == 'acc':
			self.acc += int(self.currentCode[1])
			self.codeIdx += 1
			self.currentCode = self.codeInput[self.codeIdx]
			return
		elif self.currentCode[0] == 'jmp':
			self.codeIdx += int(self.currentCode[1])
			self.currentCode = self.codeInput[self.codeIdx]
			return

c = OpCode(myInput)

while c.loopComplete == False:
	c.execute()

print(c.acc)


		

	