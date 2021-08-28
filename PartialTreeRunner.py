from TreeRunner import TreeRunner
from NodeInstructions import FullRetroTree
from NodeInstructions import Instruction
from NodeInstructions import PartialRetroTree
from NodeInstructions import PartialRetroTreeRollback
from NodeInstructions import TimeSlot_Instructions
import random
import config

class PartialTreeRunner(TreeRunner):
    def __init__(self) :
        super ().__init__ ()


    def Run1(self):
        time_slots = 20
        updates_per_time = 3
        retro_start = 1
        retro_end = 2
        averages = 1

        self.rollback_method ( averages, retro_end, retro_start, time_slots, updates_per_time )

        #self.standard_method ( averages, retro_end, retro_start, time_slots, updates_per_time )

    def standard_method(self, averages, retro_end, retro_start, time_slots, updates_per_time) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTree ()
            tm += self.base_run1 ( tl, time_slots, updates_per_time, retro_start, retro_end )
        tm = tm / averages
        print ( "Total Time Standard: {0}".format ( tm ) )

    def rollback_method(self, averages, retro_end, retro_start, time_slots, updates_per_time) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTreeRollback ()
            tm += self.base_run1 ( tl, time_slots, updates_per_time, retro_start, retro_end )
            tl = None
        #tm = tm / averages
        print ( "Total Time Rollback: {0}".format ( tm ) )
        print("Timer B: {0}, Timer C:{1}".format(config.timer_B, config.timer_C))



