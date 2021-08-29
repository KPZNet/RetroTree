import copy
import gc
import pandas as pd
from NodeInstructions import PartialRetroTree
from NodeInstructions import PartialRetroTreeRollback
from TreeRunner import TreeRunner


class PartialTreeRunner ( TreeRunner ) :
    def __init__(self) :
        super ().__init__ ()

    def Run1(self) :
        time_slots = 100
        update_size = 10
        averages = 10

        tester = TreeRunner ()
        times1, times2 = tester.build_test_times ( 0, time_slots, update_size, 1, 5000 )

        run_times = pd.DataFrame ()
        rollback_times = []
        standard_times = []
        for s in list ( range ( 0, time_slots - 1 ) ) :
            gc.collect ()
            timesback = times2[s :s + 1]
            trollback = self.rollback_method ( averages, times1, timesback )
            tstandard = self.standard_method ( averages, times1, timesback )
            rollback_times.append ( trollback )
            standard_times.append ( tstandard )

            print ( "Time:{0}, Slice:{1}:{2}".format ( s, s, s + 1 ) )
            print ( "Rollback: {0}".format ( trollback ) )
            print ( "Standard: {0}".format ( tstandard ) )

        run_times["Times"] = list ( range ( 0, time_slots - 1 ) )
        run_times["Rollback"] = rollback_times
        run_times["Standard"] = standard_times

        return run_times

    def rollback_method(self, averages, times1, times2) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTreeRollback ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ), copy.deepcopy ( times2 ) )
        return tm / averages

    def standard_method(self, averages, times1, times2) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTree ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ), copy.deepcopy ( times2 ) )
        return tm / averages
