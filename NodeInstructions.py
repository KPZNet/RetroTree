from BSTree import BSTree

class Bst_Instruction :
	# Constructor to create a new time node
	def __init__(self, inst, key, payload=None) :
		self.instructionCode = inst
		self.key = key
		self.payload = payload
		if payload == None:
			self.payload = key
		self.bst = None

class Bst_InstructionList:
	def __init__(self, _time) :
		self.instructions = []
		self.time = _time
		self.bst = BSTree()
	def addInstruction(self, instruction):
		self.instructions.append(instruction)


class TimeLine:
	def __init__(self) :
		self.instructions = []
		self.bst = None

	def ReplayInstruction(self, bst, time_slot):
		for inst in time_slot.instructions:
			if inst.instructionCode == "add":
				bst.insert(inst.key, inst.payload)
			if inst.instructionCode == "del":
				bst.deleteNode ( inst.key )
		return bst

	def __sf(self, e) :
		return e.time


	def addInstructions(self, inst):
		self.instructions.append(inst)
		self.instructions.sort(key = self._TimeLine__sf)

	def buildtree(self, keeptree = False, balance="False"):
		bst = BSTree()
		for inst in self.instructions:
			self.ReplayInstruction(bst, inst)
		if balance:
			bst.rebalance()
		if keeptree:
			self.bst = bst
		return bst

	def buildtree_up_to_time(self, time, keeptree=False, balance="False"):
		bst = BSTree()
		for inst in self.instructions:
			if inst.time <= time:
				self.ReplayInstruction(bst, inst)
		if balance:
			bst.rebalance()
		if keeptree:
			self.bst = bst
		return bst
  


