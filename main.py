# A PARTIAL Binary Search Tree
# Python program to demonstrate delete operation
# in binary search tree
import random
from BSTree import BSTree
from NodeInstructions import BSTI
from NodeInstructions import BSTInstructionList

il = BSTInstructionList()

il.addInstruction(BSTI( "add", 5, 3 ))
il.addInstruction(BSTI( "add", 6, 5 ))
il.addInstruction(BSTI( "add", 7, 7 ))
il.addInstruction(BSTI( "add", 8, 1 ))
il.addInstruction(BSTI( "add", 9, 2 ))
il.addInstruction(BSTI( "add", 10, 9 ))
il.addInstruction(BSTI( "add", 11, 15 ))
il.addInstruction(BSTI( "del", 7, 17 ))
il.addInstruction(BSTI( "del", 11, 19 ))
il.addInstruction(BSTI( "add", 7, 21 ))

bt = il.buildtree(keeptree=False, balance=True)
bt.print_tree( )


