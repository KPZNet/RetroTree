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

	def ReplayInstruction(self, bst, inst):
		if inst.instructionCode == "add":
			bst.insert(inst.key)
		if inst.instructionCode == "del" :
			bst.deleteNode ( inst.key )
		return bst

	def sf(self, e) :
		return e.time

	def addInstruction(self,inst):
		self.instructions.append(inst)
		self.instructions.sort(key = self.sf)

	def buildtree(self, balance="False"):
		bst = BSTree()
		for inst in self.instructions:
			self.ReplayInstruction(bst, inst)

		if balance == True:
			bst.rebalance()
		return bst


    
  


