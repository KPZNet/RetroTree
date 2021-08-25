from NodeInstructions import FullRetroTree
from NodeInstructions import Instruction
from NodeInstructions import PartialRetroTree
from NodeInstructions import TimeSlot_Instructions


tl = FullRetroTree ()
#tl = PartialRetroTree()

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




print("------------FINAL------------\n")
latest = tl.get_latest_tree()
latest.print_tree("FINAL TREE")

print("------------TIME LINE--------\n")
tl.print_complete_time_history ()

