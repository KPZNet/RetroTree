from NodeInstructions import Instruction
from NodeInstructions import TimeLine
from NodeInstructions import TimeSlot_Instructions
from BSTree import BSTree


tl = TimeLine ()

il = TimeSlot_Instructions ( 4 )
il.addInstruction ( Instruction ( "add", 4 ) )
il.addInstruction ( Instruction ( "add", 15 ) )
il.addInstruction ( Instruction ( "add", 16 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 7 )
il.addInstruction ( Instruction ( "add", 1 ) )
il.addInstruction ( Instruction ( "add", 17 ) )
il.addInstruction ( Instruction ( "add", 2 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 8 )
il.addInstruction ( Instruction ( "add", 200 ) )
il.addInstruction ( Instruction ( "add", 201 ) )
il.addInstruction ( Instruction ( "add", 202 ) )
il.addInstruction ( Instruction ( "add", 203 ) )
il.addInstruction ( Instruction ( "add", 6 ) )
il.addInstruction ( Instruction ( "add", 205 ) )
il.addInstruction ( Instruction ( "add", 206 ) )
il.addInstruction ( Instruction ( "add", 3 ) )
il.addInstruction ( Instruction ( "add", 208 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 20 )
il.addInstruction ( Instruction ( "add", 8 ) )
il.addInstruction ( Instruction ( "add", 14 ) )
il.addInstruction ( Instruction ( "add", 18 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 15 )
il.addInstruction ( Instruction ( "add", 9 ) )
il.addInstruction ( Instruction ( "add", 301 ) )
il.addInstruction ( Instruction ( "add", 287 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 16 )
il.addInstruction ( Instruction ( "add", 19 ) )
il.addInstruction ( Instruction ( "add", 330 ) )
il.addInstruction ( Instruction ( "add", 11 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 18 )
il.addInstruction ( Instruction ( "add", 7 ) )
il.addInstruction ( Instruction ( "add", 299 ) )
il.addInstruction ( Instruction ( "add", 23 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 25 )
il.addInstruction ( Instruction ( "add", 20, "Viggo" ) )
il.addInstruction ( Instruction ( "add", 21 ) )
il.addInstruction ( Instruction ( "add", 332 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 5 )
il.addInstruction ( Instruction ( "del", 15 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 10 )
il.addInstruction ( Instruction ( "add", 15 ) )
tl.UpdateTree ( il )

il = TimeSlot_Instructions ( 24 )
il.addInstruction ( Instruction ( "del", 15 ) )
tl.UpdateTree ( il )

bt = tl.build_complete_tree ( keeptree=False, balance=False )
bt.rebalance ()
print ( "\n" )
bt.print_tree ()
print ( "\n" )

nds = tl.gettimeline ()
for time in nds :
    print ( "Time slot {0}".format ( time.payload.time ) )
    time.payload.bst.print_tree ()
    print ( "\n" )

tl.BST_TimeSlots.print_tree ()
tl.printTimeLine ()
