from NodeInstructions import Instruction
from NodeInstructions import TimeLine
from NodeInstructions import TimeSlot_Instructions
from BSTree import BSTree

def PL(l = 1):
    for i in range(l):
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

il = TimeSlot_Instructions (20)
il.addInstruction (Instruction ("add", 11))
il.addInstruction (Instruction ("add", 67))
il.addInstruction (Instruction ("add", 34))
tl.UpdateTree (il)


latestTree = tl.getlatesttree()
print("Latest TREE")
latestTree.print_tree()
PL()

print("Largest Key:{0}".format(latestTree.getlargestkey()))
print("Largest Key:{0}".format(latestTree.getsmallestkey()))

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

tback = 10
bt_copy = latestTree.copyme()
bt_copy.print_tree("FULL Copy")
bRetro = tl.rollback_to_time(bt_copy, tback)

bRetro.print_tree ("\nRetro 10")
print ("\n")


print("Timeline: \n")
tl.printTimeLine ()
