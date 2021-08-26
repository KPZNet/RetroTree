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
        
        tl = PartialRetroTree()
        tm = self.base_run1(tl, 10, 1)
        print("Total Time Partial:{0}".format(tm))        
        
        tl = PartialRetroTreeRollback()
        tm = self.base_run1(tl, 10, 1)
        print("Total Time Partial Rollback:{0}".format(tm))
        
        tl = PartialRetroTree()
        tm = self.base_run1(tl, 10, 1)
        print("Total Time Partial:{0}".format(tm))

        tl = PartialRetroTree()
        tm = self.base_run1(tl, 10, 1)
        print("Total Time Partial:{0}".format(tm))

        tl = PartialRetroTreeRollback()
        tm = self.base_run1(tl, 10, 1)
        print("Total Time Partial Rollback:{0}".format(tm))