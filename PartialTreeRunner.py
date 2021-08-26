from TreeRunner import TreeRunner
from NodeInstructions import FullRetroTree
from NodeInstructions import Instruction
from NodeInstructions import PartialRetroTree
from NodeInstructions import PartialRetroTreeRollback
from NodeInstructions import TimeSlot_Instructions
import random

class PartialTreeRunner(TreeRunner):
    def __init__(self) :
        super ().__init__ ()

    def Run1(self):
        time_slots = 50
        updates_per_time = 10
        retro_start = 1
        retro_end = 1

        tl = PartialRetroTreeRollback()
        tm = self.base_run1(tl, time_slots, updates_per_time, retro_start, retro_end)
        print("Total Time Partial Rollback:{0}".format(tm)) 
                
        tl = PartialRetroTree()
        tm = self.base_run1(tl, time_slots, updates_per_time, retro_start, retro_end)
        print("Total Time Partial:{0}".format(tm))        
        
        tl = PartialRetroTreeRollback()
        tm = self.base_run1(tl, time_slots, updates_per_time, retro_start, retro_end)
        print("Total Time Partial Rollback:{0}".format(tm))   

        tl = PartialRetroTreeRollback()
        tm = self.base_run1(tl, time_slots, updates_per_time, retro_start, retro_end)
        print("Total Time Partial Rollback:{0}".format(tm)) 
        
        tl = PartialRetroTree()
        tm = self.base_run1(tl, time_slots, updates_per_time, retro_start, retro_end)
        print("Total Time Partial:{0}".format(tm))         