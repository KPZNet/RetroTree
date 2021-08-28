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
        time_slots = 100
        update_size = 10
        averages = 10

        tester = TreeRunner()
        times1, times2 = tester.build_test_times(0, time_slots, update_size, 0, 5000)
        times2 = times2[50:51]

        rollback_time = self.updates_run(PartialRetroTreeRollback (), averages, times1, times2)
        standard_time = self.updates_run(PartialRetroTree (), averages, times1, times2 )

        print("Standard Update Time {0}".format(standard_time))
        print ("Rollback Update Time {0}".format ( rollback_time ) )

    def updates_run(self, tl, averages, times1, times2) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTreeRollback ()
            tm += self.base_run1 ( tl, times1, times2 )
            tl = None
        tm = tm / averages
        return tm


