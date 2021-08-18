from BSTree import BSTree

class BSTI :
	# Constructor to create a new time node
	def __init__(self, inst, key, time) :
		self.instructionCode = inst
		self.key = key
		self.time = time

class BSTInstructionList:
	def __init__(self) :
		self.instructions = []
		self.BSTree = None

	def ReplayInstruction(self, bst, inst):
		if inst.instructionCode == "add":
			bst.insert(inst.key)
		if inst.instructionCode == "del" :
			bst.deleteNode ( inst.key )
		return bst

	def sf(self, e) :
		return e.time

	def addInstruction(self,inst, sortlist = True):
		self.instructions.append(inst)
		if sortlist:
			self.instructions.sort(key = self.sf)

	def buildtree(self, keeptree = False, balance="False"):
		bst = BSTree()
		for inst in self.instructions:
			self.ReplayInstruction(bst, inst)
		if balance:
			bst.rebalance()
		return bst


    
  


