# A PARTIAL Binary Search Tree
# Python program to demonstrate delete operation
# in binary search tree
import random
from BSTree import BSTree
import NodeInstructions

il = BSTInstructionList()
ni = BSTNodeInstruction("add", 5, 1)
nl.addInstruction(ni)
ni = BSTNodeInstruction("add", 7, 1)
nl.addInstruction(ni)
ni = BSTNodeInstruction("del", 5, 1)
nl.addInstruction(ni)



nums = [12, 6, 18, 19, 21, 11, 3, 5]
#nums = random.sample(range(0, 100), 50)
bst = BSTree()
for num in nums:
	bst.insert(num)

bst.rebalance()
print("Balanced Tree\n")
bst.print_tree( "key", "left", "right")
print("\n")
