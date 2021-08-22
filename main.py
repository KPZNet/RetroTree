from NodeInstructions import Instruction
from NodeInstructions import TimeLine
from NodeInstructions import TimeSlot_Instructions
from BSTree import BSTree

def PL():
    print("\n")


tl = TimeLine ()

il = TimeSlot_Instructions (5)
il.addInstruction (Instruction ("add", 4))
il.addInstruction (Instruction ("add", 15))
il.addInstruction (Instruction ("add", 16))
tl.UpdateTree (il)

il = TimeSlot_Instructions (10)
il.addInstruction (Instruction ("add", 48))
il.addInstruction (Instruction ("add", 158))
il.addInstruction (Instruction ("add", 168))
tl.UpdateTree (il)

bt = tl.build_complete_tree (keeptree=False, balance=False)
bt.rebalance ()
print ("\nCOMPLETE TREE")
bt.print_tree ()
print ("\n")

print("Largest Key:{0}".format(bt.getlargestkey()))
print("Largest Key:{0}".format(bt.getsmallestkey()))

time = 12
key = 158
val = tl.Pred(158, time=time)
print("Searching for: {0} at time: {1} FOUND: {2}".format(key, time, val))
PL()

nds = tl.gettimeline ()
for time in nds:
    print ("Time slot {0}".format (time.time))
    time.bst.print_tree ()
    print ("\n")

tl.BST_TimeSlots.print_tree ()
print("\n")
tl.printTimeLine ()
