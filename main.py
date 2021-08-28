from NodeInstructions import FullRetroTree
from NodeInstructions import Instruction
from NodeInstructions import PartialRetroTree
from NodeInstructions import TimeSlot_Instructions
import random
from TreeRunner import TreeRunner
from PartialTreeRunner import PartialTreeRunner
import sys

print("Default Recursion Limit:")
print(sys.getrecursionlimit())
sys.setrecursionlimit(1000000)
print("New Recursion Limit:")
print(sys.getrecursionlimit())

def tree_run_1(tl):

    il = TimeSlot_Instructions(5)
    il.addInstruction(Instruction("add", 40))
    il.addInstruction(Instruction("add", 150))
    il.addInstruction(Instruction("add", 160))
    tl.update_tree(il)

    il = TimeSlot_Instructions(10)
    il.addInstruction(Instruction("add", 39))
    il.addInstruction(Instruction("add", 20))
    il.addInstruction(Instruction("add", 70))
    tl.update_tree(il)

    il = TimeSlot_Instructions(10)
    il.addInstruction(Instruction("add", 67))
    il.addInstruction(Instruction("add", 26))
    il.addInstruction(Instruction("add", 33))
    tl.update_tree(il)

    il = TimeSlot_Instructions(20)
    il.addInstruction(Instruction("add", 342))
    il.addInstruction(Instruction("add", 564))
    il.addInstruction(Instruction("add", 123))
    il.addInstruction(Instruction("add", 590))
    il.addInstruction(Instruction("add", 112))
    il.addInstruction(Instruction("add", 443))
    tl.update_tree(il)

    il = TimeSlot_Instructions(5)
    il.addInstruction(Instruction("del", 40))
    il.addInstruction(Instruction("del", 150))
    il.addInstruction(Instruction("del", 160))

    il = TimeSlot_Instructions(23)
    il.addInstruction(Instruction("del", 342))
    il.addInstruction(Instruction("del", 564))
    il.addInstruction(Instruction("del", 123))
    il.addInstruction(Instruction("del", 590))
    il.addInstruction(Instruction("del", 112))
    il.addInstruction(Instruction("del", 443))

    tl.update_tree(il)

    print("------------FINAL------------\n")
    latest = tl.get_latest_tree()
    latest.print_tree("FINAL TREE")



tlf = FullRetroTree ()
tlp = PartialRetroTree()

tree_run_1(tlf)
tree_run_1(tlp)



