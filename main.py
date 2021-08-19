# A PARTIAL Binary Search Tree
# Python program to demonstrate delete operation
# in binary search tree
import random
from BSTree import BSTree
from NodeInstructions import Bst_Instruction
from NodeInstructions import TimeLine

il = TimeLine()

il.addInstruction(Bst_Instruction("add", 1, 1))
il.addInstruction(Bst_Instruction("add", 2, 2))
il.addInstruction(Bst_Instruction("add", 3, 3))
il.addInstruction(Bst_Instruction("add", 4, 4))
il.addInstruction(Bst_Instruction("add", 5, 5))
il.addInstruction(Bst_Instruction("add", 6, 6))
il.addInstruction(Bst_Instruction("add", 7, 7))
il.addInstruction(Bst_Instruction("add", 8, 8))
il.addInstruction(Bst_Instruction("add", 9, 9))
il.addInstruction(Bst_Instruction("add", 10, 10))
il.addInstruction(Bst_Instruction("add", 11, 11))
il.addInstruction(Bst_Instruction("add", 12, 12))
il.addInstruction(Bst_Instruction("add", 13, 13))
il.addInstruction(Bst_Instruction("add", 14, 14))
il.addInstruction(Bst_Instruction("add", 15, 15))
il.addInstruction(Bst_Instruction("add", 16, 16))
il.addInstruction(Bst_Instruction("add", 17, 17))
il.addInstruction(Bst_Instruction("add", 18, 18))
il.addInstruction(Bst_Instruction("add", 19, 19))
il.addInstruction(Bst_Instruction("add", 20, 20))
il.addInstruction(Bst_Instruction("add", 21, 21))
il.addInstruction(Bst_Instruction("add", 22, 22))
il.addInstruction(Bst_Instruction("add", 23, 23))


bt = il.buildtree(keeptree=False, balance=True)
bt.print_tree( )


print( bt.inorder() )


