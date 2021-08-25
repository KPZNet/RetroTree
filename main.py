from NodeInstructions import Instruction
from NodeInstructions import TimeSlot_Instructions
from NodeInstructions import FullRetroTree
from NodeInstructions import PartialRetroTree


def PL():
    print("\n")


tl = FullRetroTree ()
# tl = PartialRetroTree()

il = TimeSlot_Instructions (5)
il.addInstruction (Instruction ("add", 4))
il.addInstruction (Instruction ("add", 15))
il.addInstruction (Instruction ("add", 16))
tl.update_tree (il)
tl.print_current_tree()

il = TimeSlot_Instructions (10)
il.addInstruction (Instruction ("add", 48))
il.addInstruction (Instruction ("add", 2))
il.addInstruction (Instruction ("add", 3))
tl.update_tree (il)
tl.print_current_tree()

il = TimeSlot_Instructions (15)
il.addInstruction (Instruction ("add", 485))
il.addInstruction (Instruction ("add", 1))
il.addInstruction (Instruction ("add", 41))
tl.update_tree (il)
tl.print_current_tree()

il = TimeSlot_Instructions (20)
il.addInstruction (Instruction ("add", 11))
il.addInstruction (Instruction ("add", 67))
il.addInstruction (Instruction ("add", 34))
tl.update_tree (il)
tl.print_current_tree()

il = TimeSlot_Instructions (10)
il.addInstruction (Instruction ("del", 48))
il.addInstruction (Instruction ("add", 300))
il.addInstruction (Instruction ("del", 15))
il.addInstruction (Instruction ("add", 500))
tl.update_tree (il)
tl.print_current_tree()

il = TimeSlot_Instructions (12)
il.addInstruction (Instruction ("add", 200))
il.addInstruction (Instruction ("del", 11))
il.addInstruction (Instruction ("add", 120))
tl.update_tree (il)
tl.print_current_tree()

latest = tl.get_latest_tree()
latest.print_tree("FINAL TREE")

print("Timeline: \n")
tl.print_complete_time_history ()

tl.print_timeline_trees()
