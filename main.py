from NodeInstructions import Instruction
from NodeInstructions import TimeLine
from NodeInstructions import TimeSlot_Instructions
from BSTree import BSTree


tl = TimeLine ()

il = TimeSlot_Instructions ( 5 )
il.addInstruction ( Instruction ( "add", 4 ) )
il.addInstruction ( Instruction ( "add", 15 ) )
il.addInstruction ( Instruction ( "add", 16 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 10 )
il.addInstruction ( Instruction ( "add", 48 ) )
il.addInstruction ( Instruction ( "add", 158 ) )
il.addInstruction ( Instruction ( "add", 168 ) )
tl.UpdateTree ( il )


bt = tl.build_complete_tree ( keeptree=False, balance=False )
bt.rebalance ()
print ( "\n" )
bt.print_tree ()
print ( "\n" )

print( bt.getlargestkey() )
print( bt.getsmallestkey() )

val = tl.Pred(6, time=33)
print("Value found at time is {0}".format(val))
exit(0)

nds = tl.gettimeline ()
for time in nds :
    print ( "Time slot {0}".format ( time.time ) )
    time.bst.print_tree ()
    print ( "\n" )

tl.BST_TimeSlots.print_tree ()
print("\n")
tl.printTimeLine ()
