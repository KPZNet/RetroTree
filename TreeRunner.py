from NodeInstructions import Instruction
from NodeInstructions import TimeSlot_Instructions

from NodeInstructions import FullRetroTree
from NodeInstructions import Instruction
from NodeInstructions import PartialRetroTree
from NodeInstructions import PartialRetroTreeRollback
from NodeInstructions import TimeSlot_Instructions

import time
import random

NANO_TO_MS = 1000000

class TreeRunner:
    def __init__(self):
        self.retro_tree_time1 = 0
        self.retro_tree_time2 = 0
        self.full_tree_time1 = 0
        self.rull_tree_time2 = 0


    def test_tree(self):
        tl = PartialRetroTree()

        il = TimeSlot_Instructions ( 5 )
        il.addInstruction ( Instruction ( "add", 40 ) )
        il.addInstruction ( Instruction ( "add", 150 ) )
        il.addInstruction ( Instruction ( "add", 160 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update at 5: " )

        il = TimeSlot_Instructions ( 10 )
        il.addInstruction ( Instruction ( "add", 39 ) )
        il.addInstruction ( Instruction ( "add", 20 ) )
        il.addInstruction ( Instruction ( "add", 70 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update Time 10: " )

        il = TimeSlot_Instructions ( 20 )
        il.addInstruction ( Instruction ( "add", 67 ) )
        il.addInstruction ( Instruction ( "add", 26 ) )
        il.addInstruction ( Instruction ( "add", 33 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update Time 20: " )

        il = TimeSlot_Instructions ( 15 )
        il.addInstruction ( Instruction ( "del", 20 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update Time 15: " )

        print ( "------------TIME LINE--------\n" )
        tl.print_complete_time_history ()

        print ( "------------FINAL------------\n" )
        latest = tl.get_latest_tree ()
        latest.print_tree ( "FINAL TREE" )


    def base_run1(self, tl, runs, updates_per_time, retro_start, retro_end):
        
        for run in list( range ( 0, runs ) ):
            il = TimeSlot_Instructions ( run )
            start = 0 + (updates_per_time*run)
            end = updates_per_time + (updates_per_time*run)
            datList = list( range ( start, end ) )
            for n in datList:
                il.addInstruction ( Instruction ( "add", n ) )
            tl.update_tree(il)
        
        start_time = time.perf_counter_ns ()
        
        for run in list( range ( retro_start, retro_end ) ):
            il = TimeSlot_Instructions ( run )
            start = 0 + (updates_per_time*run)
            end = updates_per_time + (updates_per_time*run)
            datList = list( range ( start, end ) )
            for n in datList:
                il.addInstruction ( Instruction ( "del", n ) )
            tl.update_tree(il)
            
        stop_time = time.perf_counter_ns ()
        ls_timing = (stop_time - start_time) / NANO_TO_MS
        return ls_timing
    
