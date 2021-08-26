from NodeInstructions import Instruction
from NodeInstructions import TimeSlot_Instructions


class TreeRunner:
    def __init__(self):
        self.retro_tree_time1 = 0
        self.retro_tree_time2 = 0
        self.full_tree_time1 = 0
        self.rull_tree_time2 = 0

    def base_run1(self, tl):
        il = TimeSlot_Instructions ( 5 )

        datList = list( range ( 1, 128 ) )
        for n in datList:
            il.addInstruction ( Instruction ( "add", n ) )
        tl.update_tree(il)

        print ( "------------TIME LINE--------\n" )
        tl.print_complete_time_history ()

        print ( "------------FINAL------------\n" )
        latest = tl.get_latest_tree ()
        latest.print_tree ( "FINAL TREE" )