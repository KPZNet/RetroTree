from NodeInstructions import FullRetroTree
from NodeInstructions import Instruction
from NodeInstructions import PartialRetroTree
from NodeInstructions import TimeSlot_Instructions
import random


tl = FullRetroTree ()
#tl = PartialRetroTree()

TreeSize = 10000
keyRange = 1000000
il = TimeSlot_Instructions (10)
for i in range(TreeSize):
    rando = random.randint(1, keyRange)
    il.addInstruction(Instruction("add", rando))
tl.update_tree (il)

il = TimeSlot_Instructions (20)
for i in range(TreeSize):
    rando = random.randint(keyRange, keyRange*2)
    il.addInstruction(Instruction("add", rando))
tl.update_tree (il)

il = TimeSlot_Instructions (30)
for i in range(TreeSize):
    rando = random.randint(keyRange*3, keyRange*4)
    il.addInstruction(Instruction("add", rando))
tl.update_tree (il)

tl.BST_TimeSlots.rebalance()
exit(0)


il = TimeSlot_Instructions (5)
il.addInstruction (Instruction ("add", 40))
il.addInstruction (Instruction ("add", 150))
il.addInstruction (Instruction ("add", 160))
tl.update_tree (il)
tl.print_current_tree("Update at 5: ")

il = TimeSlot_Instructions (10)
il.addInstruction (Instruction ("add", 39))
il.addInstruction (Instruction ("add", 20))
il.addInstruction (Instruction ("add", 70))
tl.update_tree (il)
tl.print_current_tree("Update Time 10: ")

il = TimeSlot_Instructions (20)
il.addInstruction (Instruction ("add", 67))
il.addInstruction (Instruction ("add", 26))
il.addInstruction (Instruction ("add", 33))
tl.update_tree (il)
tl.print_current_tree("Update Time 20: ")

il = TimeSlot_Instructions (15)
il.addInstruction (Instruction ("del", 20))
tl.update_tree (il)
tl.print_current_tree("Update Time 15: ")


print("------------TIME LINE--------\n")
tl.print_complete_time_history ()

print("------------FINAL------------\n")
latest = tl.get_latest_tree()
latest.print_tree("FINAL TREE")