from BSTree import BSTree

class Bst_Instruction :
	# Constructor to create a new time node
	def __init__(self, inst, time, key, payload=None) :
		self.instructionCode = inst
		self.time = time
		self.key = key
		self.payload = payload
		if payload == None:
			self.payload = key
		self.bst = None
		

class TimeLine:
	def __init__(self) :
		self.instructions = []
		self.bst = None
		self.bst = 0
		self.current_time = 1

	def ReplayInstruction(self, bst, inst):
		if inst.instructionCode == "add":
			bst.insert(inst.key, inst.payload)
		if inst.instructionCode == "del" :
			bst.deleteNode ( inst.key )
		return bst

	def __sf(self, e) :
		return e.time


	def addInstruction(self, inst, sortlist = True):
		if inst.time is None:
			inst.time = self.current_time
			self.current_time = self.current_time + 1
		self.instructions.append(inst)
		if sortlist:
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
  


