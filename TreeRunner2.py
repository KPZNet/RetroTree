import copy
import gc
import random
import time
from datetime import datetime


import matplotlib.pyplot as plt
import pandas as pd

import config
from RetroBSTrees import *

NANO_TO_MS = 1000000




class TreeRunner2 :
    def __init__(self) :
        random.seed ( datetime.now () )

    def build_test_times2(self, start_time, end_time, random_start, random_end) :
        timeslistAdd = []
        random_set = set ()
        for n in list ( range ( start_time, end_time ) ) :
            rlist = random.sample ( range ( random_start, random_end ), n )
            rlist = list ( set ( rlist ) )
            already_used_set = set ( random_set ).intersection ( rlist )
            randomlist = list ( set ( rlist ).symmetric_difference ( already_used_set ) )
            random_set = random_set.union ( randomlist )
            il = TimeSlot_Instructions ( n )
            for r in randomlist :
                il.addInstruction ( Instruction ( "add", r ) )
            timeslistAdd.append ( il )
        return timeslistAdd

    def base_run1(self, tl, times1) :
        #gc.collect()
        config.timer_A = 0.0
        start_time = time.perf_counter_ns ()
        tl.update_tree ( times1 )
        config.timer_A += ((time.perf_counter_ns () - start_time) / NANO_TO_MS)
        return config.timer_A

    def plot_comparison_runs(self, rts) :
        plt.plot ( rts["Times"], rts["PartialRollback"], label="Partial Rollback" )
        plt.plot ( rts["Times"], rts["PartialStandard"], label="Partial Standard" )
        plt.title ( "Run ADD for PARTIAL Retro-BST" )
        plt.xlabel ( "Retro ADD Times" )
        plt.ylabel ( "milliseconds" )
        plt.legend ()
        plt.show ()

        plt.plot ( rts["Times"], rts["FullRollback"], label="Full Rollback" )
        plt.plot ( rts["Times"], rts["FullStandard"], label="Full Standard" )
        plt.title ( "Run ADD for FULL Retro-BST" )
        plt.xlabel ( "Retro ADD Times" )
        plt.ylabel ( "milliseconds" )
        plt.legend ()
        plt.show ()

    def Run(self) :
        rts = self.UpdateSlideOverTime ()
        self.plot_comparison_runs ( rts )

    def UpdateSlideOverTime(self) :
        time_slots = 100
        averages = 20

        times1 = self.build_test_times2 ( 0, time_slots, 1, 1000000 )

        run_times = pd.DataFrame ()
        partial_rollback_times = []
        partial_standard_times = []
        full_rollback_times = []
        full_standard_times = []
        for s in times1:

            partial_trollback = self.partial_rollback_method (averages, s)
            partial_tstandard = self.partial_standard_method (averages, s)

            full_trollback = self.full_rollback_method (averages, s)
            full_tstandard = self.full_standard_method (averages, s)

            partial_rollback_times.append ( partial_trollback )
            partial_standard_times.append ( partial_tstandard )

            full_rollback_times.append ( full_trollback )
            full_standard_times.append ( full_tstandard )

            print ( "Time:{0}".format(len(s.instructions)) )
            print ( "PARTIAL update: {0}".format ( partial_trollback ) )
            print ( "PARTIAL update: {0}".format ( partial_tstandard ) )
            print ( "FULL update: {0}".format ( full_trollback ) )
            print ( "FULL update: {0}".format ( full_tstandard ) )

        run_times["Times"] = list ( range ( 0, len(times1) ) )
        run_times["PartialRollback"] = partial_rollback_times
        run_times["PartialStandard"] = partial_standard_times
        run_times["FullRollback"] = full_rollback_times
        run_times["FullStandard"] = full_standard_times

        return run_times

    def partial_rollback_method(self, averages, times1) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTreeRollback ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ) )
        return tm / averages

    def partial_standard_method(self, averages, times1) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTree ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ) )
        return tm / averages

    def full_rollback_method(self, averages, times1) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = FullRetroTreeRollback ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ) )
        return tm / averages

    def full_standard_method(self, averages, times1) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = FullRetroTree ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ) )
        return tm / averages