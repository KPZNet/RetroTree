import pandas as pd
from NodeInstructions import Instruction
from NodeInstructions import TimeLine
from NodeInstructions import TimeSlot_Instructions

tl = TimeLine ()

il = TimeSlot_Instructions ( 2 )
il.addInstruction ( Instruction ( "add", 4 ) )
il.addInstruction ( Instruction ( "add", 15 ) )
il.addInstruction ( Instruction ( "add", 16 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 5 )
il.addInstruction ( Instruction ( "add", 1 ) )
il.addInstruction ( Instruction ( "add", 17 ) )
il.addInstruction ( Instruction ( "add", 2 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 8 )
il.addInstruction ( Instruction ( "add", 23 ) )
il.addInstruction ( Instruction ( "add", 34 ) )
il.addInstruction ( Instruction ( "add", 112 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 20 )
il.addInstruction ( Instruction ( "add", 8 ) )
il.addInstruction ( Instruction ( "add", 14 ) )
il.addInstruction ( Instruction ( "add", 18 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 15 )
il.addInstruction ( Instruction ( "add", 9 ) )
il.addInstruction ( Instruction ( "add", 165 ) )
il.addInstruction ( Instruction ( "add", 287 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 16 )
il.addInstruction ( Instruction ( "add", 19 ) )
il.addInstruction ( Instruction ( "add", 10 ) )
il.addInstruction ( Instruction ( "add", 11 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 18 )
il.addInstruction ( Instruction ( "add", 7 ) )
il.addInstruction ( Instruction ( "add", 22 ) )
il.addInstruction ( Instruction ( "add", 23 ) )
tl.Add_TimeSlot_Instructions ( il )


il = TimeSlot_Instructions ( 25 )
il.addInstruction ( Instruction ( "add", 20, "Viggo" ) )
il.addInstruction ( Instruction ( "add", 21 ) )
il.addInstruction ( Instruction ( "add", 332 ) )
tl.Add_TimeSlot_Instructions ( il )

bt = tl.buildtree ( keeptree=False, balance=False )
bt.print_tree ()
bt.rebalance()
bt.print_tree()


df = tl.gettimelinedf()
print(df)
