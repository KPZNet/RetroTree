from BSTree import BSTree

class BSTI :
	# Constructor to create a new time node
	def __init__(self, inst, time, key, payload=None) :
		self.instructionCode = inst
		self.time = time
		self.key = key
		self.payload = payload
		if payload == None:
			self.payload = key
		

class BSTInstructionList:
	def __init__(self) :
		self.instructions = []
		self.bst = None

	def ReplayInstruction(self, bst, inst):
		if inst.instructionCode == "add":
			bst.insert(inst.key, inst.payload)
		if inst.instructionCode == "del" :
			bst.deleteNode ( inst.key )
		return bst

	def __sf(self, e) :
		return e.time


	def addInstruction(self,inst, sortlist = True):
		self.instructions.append(inst)
		if sortlist:
			self.instructions.sort(key = self._BSTInstructionList__sf)

	def buildtree(self, keeptree = False, balance="False"):
		bst = BSTree()
		for inst in self.instructions:
			self.ReplayInstruction(bst, inst)
		if balance:
			bst.rebalance()
		if keeptree:
			self.bst = bst
		return bst


    
  


