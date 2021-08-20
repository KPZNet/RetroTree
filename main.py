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

il2 = TimeSlot_Instructions ( 5 )
il2.addInstruction ( Instruction ( "add", 1 ) )
il2.addInstruction ( Instruction ( "add", 17 ) )
il2.addInstruction ( Instruction ( "add", 2 ) )
il2.addInstruction ( Instruction ( "add", 3 ) )
il2.addInstruction ( Instruction ( "add", 22 ) )
tl.Add_TimeSlot_Instructions ( il2 )

il3 = TimeSlot_Instructions ( 8 )
il3.addInstruction ( Instruction ( "add", 23 ) )
tl.Add_TimeSlot_Instructions ( il3 )

il = TimeSlot_Instructions ( 15 )
il.addInstruction ( Instruction ( "add", 9 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 16 )
il.addInstruction ( Instruction ( "add", 19 ) )
il.addInstruction ( Instruction ( "add", 10 ) )
il.addInstruction ( Instruction ( "add", 11 ) )
il.addInstruction ( Instruction ( "add", 12 ) )
il.addInstruction ( Instruction ( "add", 13 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 18 )
il.addInstruction ( Instruction ( "add", 7 ) )
il.addInstruction ( Instruction ( "add", 22 ) )
il.addInstruction ( Instruction ( "add", 23 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 20 )
il.addInstruction ( Instruction ( "add", 8 ) )
il.addInstruction ( Instruction ( "add", 14 ) )
il.addInstruction ( Instruction ( "add", 18 ) )
tl.Add_TimeSlot_Instructions ( il )

il = TimeSlot_Instructions ( 25 )
il.addInstruction ( Instruction ( "add", 20, "Viggo" ) )
il.addInstruction ( Instruction ( "add", 21 ) )
tl.Add_TimeSlot_Instructions ( il )



bt = tl.buildtree ( keeptree=False, balance=False )
bt.print_tree ()
bt.rebalance()
bt.print_tree()


df = tl.gettimelinedf()
print(df)
