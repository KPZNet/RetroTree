# A PARTIAL Binary Search Tree
# Python program to demonstrate delete operation
# in binary search tree
import random
from BSTree import BSTree
from NodeInstructions import Bst_Instruction
from NodeInstructions import TimeLine

il = TimeLine()

il.addInstruction(Bst_Instruction("add", None, 1))
il.addInstruction(Bst_Instruction("add", None, 2))
il.addInstruction(Bst_Instruction("add", None, 3))
il.addInstruction(Bst_Instruction("add", None, 4))
il.addInstruction(Bst_Instruction("add", None, 5))
il.addInstruction(Bst_Instruction("add", None, 6))
il.addInstruction(Bst_Instruction("add", None, 7))
il.addInstruction(Bst_Instruction("add", None, 8))
il.addInstruction(Bst_Instruction("add", None, 9))
il.addInstruction(Bst_Instruction("add", None, 10))
il.addInstruction(Bst_Instruction("add", None, 11))
il.addInstruction(Bst_Instruction("add", None, 12))
il.addInstruction(Bst_Instruction("add", None, 13))
il.addInstruction(Bst_Instruction("add", None, 14))
il.addInstruction(Bst_Instruction("add", None, 15))
il.addInstruction(Bst_Instruction("add", None, 16))
il.addInstruction(Bst_Instruction("add", None, 17))
il.addInstruction(Bst_Instruction("add", None, 18))
il.addInstruction(Bst_Instruction("add", None, 19))
il.addInstruction(Bst_Instruction("add", None, 20, "V"))
il.addInstruction(Bst_Instruction("add", None, 21))
il.addInstruction(Bst_Instruction("add", None, 22))
il.addInstruction(Bst_Instruction("add", None, 23))


bt = il.buildtree(keeptree=False, balance=True)
bt2 = bt.copytree()

bt.print_tree()
bt2.print_tree()

s = bt.search(20)
print(s)
s2 = bt2.search(20)
print(s2)




