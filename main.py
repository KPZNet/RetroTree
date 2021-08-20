import pandas as pd
from NodeInstructions import Instruction
from NodeInstructions import TimeLine
from NodeInstructions import TimeSlot_Instructions

il = TimeSlot_Instructions ( 50 )

il.addInstruction ( Instruction ( "add", 4 ) )
il.addInstruction ( Instruction ( "add", 15 ) )
il.addInstruction ( Instruction ( "add", 16 ) )
il.addInstruction ( Instruction ( "add", 1 ) )
il.addInstruction ( Instruction ( "add", 17 ) )
il.addInstruction ( Instruction ( "add", 2 ) )
il.addInstruction ( Instruction ( "add", 3 ) )
il.addInstruction ( Instruction ( "add", 22 ) )
il.addInstruction ( Instruction ( "add", 23 ) )
il.addInstruction ( Instruction ( "add", 9 ) )
il.addInstruction ( Instruction ( "add", 19 ) )
il.addInstruction ( Instruction ( "add", 10 ) )
il.addInstruction ( Instruction ( "add", 11 ) )
il.addInstruction ( Instruction ( "add", 12 ) )
il.addInstruction ( Instruction ( "add", 13 ) )
il.addInstruction ( Instruction ( "add", 7 ) )
il.addInstruction ( Instruction ( "add", 22 ) )
il.addInstruction ( Instruction ( "add", 23 ) )
il.addInstruction ( Instruction ( "add", 8 ) )
il.addInstruction ( Instruction ( "add", 14 ) )
il.addInstruction ( Instruction ( "add", 18 ) )
il.addInstruction ( Instruction ( "add", 20, "Viggo" ) )
il.addInstruction ( Instruction ( "add", 21 ) )

tl = TimeLine ()
tl.Add_TimeSlot_Instructions ( il )

bt = tl.buildtree ( keeptree=False, balance=False )
bt2 = bt.copytree ()

bt.print_tree ()
bt2.print_tree ()

bt2.rebalance ()
bt.print_tree ()
bt2.print_tree ()

df = tl.gettimelinedf()

print(df)
