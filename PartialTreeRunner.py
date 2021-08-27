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
        updates_per_time = 5
        retro_start = 48
        retro_end = 49
        averages = 20

        tm = 0.0
        for i in list( range(averages)):
            tl = PartialRetroTree()
            tm += self.base_run1(tl, time_slots, updates_per_time, retro_start, retro_end)
        tm = tm/averages
        print("Total Time Standard: {0}".format(tm))

        tm = 0.0
        for i in list( range(averages)):
            tl = PartialRetroTreeRollback()
            tm += self.base_run1(tl, time_slots, updates_per_time, retro_start, retro_end)
        tm = tm/averages
        print("Total Time Rollback: {0}".format(tm))


