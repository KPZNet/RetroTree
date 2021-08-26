from NodeInstructions import Instruction
from NodeInstructions import TimeSlot_Instructions
import time

NANO_TO_MS = 1000000

class TreeRunner:
    def __init__(self):
        self.retro_tree_time1 = 0
        self.retro_tree_time2 = 0
        self.full_tree_time1 = 0
        self.rull_tree_time2 = 0

    def base_run1(self, tl, updates_per_time, runs):
        
        for run in list( range ( 0, runs ) ):
            il = TimeSlot_Instructions ( run )
            start = 0 + (updates_per_time*run)
            end = updates_per_time + (updates_per_time*run)
            datList = list( range ( start, end ) )
            for n in datList:
                il.addInstruction ( Instruction ( "add", n ) )
            tl.update_tree(il)
        
        start_time = time.perf_counter_ns ()
        
        for run in list( range ( int(runs/2), runs ) ):
            il = TimeSlot_Instructions ( run )
            start = 0 + (updates_per_time*run)
            end = updates_per_time + (updates_per_time*run)
            datList = list( range ( start, end ) )
            for n in datList:
                il.addInstruction ( Instruction ( "del", n ) )
            tl.update_tree(il)

        l = tl.current_tree.inorder()
        ll = len(l)        
        
        stop_time = time.perf_counter_ns ()
        ls_timing = (stop_time - start_time) / NANO_TO_MS
        return ls_timing
    
