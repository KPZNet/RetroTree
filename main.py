# A PARTIAL Binary Search Tree
# Python program to demonstrate delete operation
# in binary search tree
import random
from BSTree import BSTree
from NodeInstructions import Bst_Instruction
from NodeInstructions import TimeLine

il = TimeLine()

il.addInstruction(Bst_Instruction("add", 20, 1))
il.addInstruction(Bst_Instruction("add", 20, 2))
il.addInstruction(Bst_Instruction("add", 20, 3))
il.addInstruction(Bst_Instruction("add", 20, 4))
il.addInstruction(Bst_Instruction("add", 20, 5))
il.addInstruction(Bst_Instruction("add", 20, 6))
il.addInstruction(Bst_Instruction("add", 20, 7))
il.addInstruction(Bst_Instruction("add", 20, 8))
il.addInstruction(Bst_Instruction("add", 20, 9))
il.addInstruction(Bst_Instruction("add", 20, 10))
il.addInstruction(Bst_Instruction("add", 20, 11))
il.addInstruction(Bst_Instruction("add", 20, 12))
il.addInstruction(Bst_Instruction("add", 20, 13))
il.addInstruction(Bst_Instruction("add", 20, 14))
il.addInstruction(Bst_Instruction("add", 20, 15))
il.addInstruction(Bst_Instruction("add", 20, 16))
il.addInstruction(Bst_Instruction("add", 20, 17))
il.addInstruction(Bst_Instruction("add", 20, 18))
il.addInstruction(Bst_Instruction("add", 20, 19))
il.addInstruction(Bst_Instruction("add", 20, 20))
il.addInstruction(Bst_Instruction("add", 20, 21))
il.addInstruction(Bst_Instruction("add", 20, 22))
il.addInstruction(Bst_Instruction("add", 20, 23))


bt = il.buildtree(keeptree=False, balance=True)
bt.print_tree( )

pl = bt.search(2)
print(pl)

pln = bt.findmax(17)
print(pln)



