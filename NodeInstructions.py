from BSTree import BSTree

class BSTNodeInstruction :
	# Constructor to create a new time node
	def __init__(self, inst, key, time) :
		self.instructionCode = "none"
		self.key = 0
		self.time = 0

class BSTInstructionList:
  instructions = []
  
  def addInstruction(inst):
    instructions.prepend(inst)
    instructions.sort(key = lamdba x:x.time)


    
  


