# A PARTIAL Binary Search Tree
# Python program to demonstrate delete operation
# in binary search tree
import random
from BSTree import BSTree
from NodeInstructions import Bst_Instruction
from NodeInstructions import Bst_InstructionList
from NodeInstructions import TimeLine

il = Bst_InstructionList(50)

il.addInstruction(Bst_Instruction("add", 4))
il.addInstruction(Bst_Instruction("add", 15))
il.addInstruction(Bst_Instruction("add", 16))
il.addInstruction(Bst_Instruction("add", 1))
il.addInstruction(Bst_Instruction("add", 17))
il.addInstruction(Bst_Instruction("add", 2))
il.addInstruction(Bst_Instruction("add", 3))
il.addInstruction(Bst_Instruction("add", 22))
il.addInstruction(Bst_Instruction("add", 23))
il.addInstruction(Bst_Instruction("add", 9))
il.addInstruction(Bst_Instruction("add", 19))
il.addInstruction(Bst_Instruction("add", 10))
il.addInstruction(Bst_Instruction("add", 11))
il.addInstruction(Bst_Instruction("add", 12))
il.addInstruction(Bst_Instruction("add", 13))
il.addInstruction(Bst_Instruction("add", 7))
il.addInstruction(Bst_Instruction("add", 22))
il.addInstruction(Bst_Instruction("add", 23))
il.addInstruction(Bst_Instruction("add", 8))
il.addInstruction(Bst_Instruction("add", 14))
il.addInstruction(Bst_Instruction("add", 18))
il.addInstruction(Bst_Instruction("add", 20, "Viggo"))
il.addInstruction(Bst_Instruction("add", 21))

tl = TimeLine()
tl.addInstructions(il)



bt = tl.buildtree(keeptree=False, balance=False)
bt2 = bt.copytree()

bt.print_tree()
bt2.print_tree()

bt2.rebalance()
bt.print_tree()
bt2.print_tree()






