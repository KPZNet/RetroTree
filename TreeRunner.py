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


def build_test_times(start_time, end_time, update_size, random_start, random_end):
    timeslistAdd = []
    timeslistDel = []
    random_set = set()
    for n in list(range(start_time, end_time)):
        rlist = random.sample(range(random_start, random_end), update_size)
        rlist = list(set(rlist))
        already_used_set = set(random_set).intersection(rlist)
        randomlist = list(set(rlist).symmetric_difference(already_used_set))
        random_set = random_set.union(randomlist)
        il = TimeSlot_Instructions(n)
        ilDel = TimeSlot_Instructions(n)
        for r in randomlist:
            il.addInstruction(Instruction("add", r))
            ilDel.addInstruction(Instruction("del", r))
        timeslistAdd.append(il)
        timeslistDel.append(ilDel)
    return timeslistAdd, timeslistDel

class TreeRunner :
    def __init__(self) :
        random.seed ( datetime.now () )


    def base_run1(self, tl, times1, times2) :

        for timeslot in times1 :
            tl.update_tree ( timeslot )

        config.timer_A = 0.0
        for timeslot in times2 :
            gc.collect()
            start_time = time.perf_counter_ns ()
            tl.update_tree ( timeslot )
            config.timer_A += ((time.perf_counter_ns () - start_time) / NANO_TO_MS)
        return config.timer_A

    def plot_comparison_runs(self, rts) :
        plt.plot ( rts["Times"], rts["PartialRollback"], label="Partial Rollback" )
        plt.plot ( rts["Times"], rts["PartialStandard"], label="Partial Standard" )
        plt.title ( "Run times for PARTIAL Retro-BST" )
        plt.xlabel ( "Retro Update Times" )
        plt.ylabel ( "milliseconds" )
        plt.legend ()
        plt.show ()

        plt.plot ( rts["Times"], rts["FullRollback"], label="Full Rollback" )
        plt.plot ( rts["Times"], rts["FullStandard"], label="Full Standard" )
        plt.title ( "Run times for FULL Retro-BST" )
        plt.xlabel ( "Retro Update Times" )
        plt.ylabel ( "milliseconds" )
        plt.legend ()
        plt.show ()

    def Partial_Comparison_rollback_runs(self) :
        rts = self.Partial_RunUp_Back_A ()
        self.plot_comparison_runs ( rts )

    def Partial_RunUp_Back_A(self) :
        time_slots = 50
        update_size = 5
        averages = 5

        times1, times2 = build_test_times ( 0, time_slots, update_size, 1, 5000 )

        run_times = pd.DataFrame ()
        partial_rollback_times = []
        partial_standard_times = []
        full_rollback_times = []
        full_standard_times = []
        for s in list ( range ( 0, time_slots - 1 ) ) :

            timesback = times2[s :s + 1]
            partial_trollback = self.partial_rollback_method (averages, times1, timesback)
            partial_tstandard = self.partial_standard_method (averages, times1, timesback)

            full_trollback = self.full_rollback_method (averages, times1, timesback)
            full_tstandard = self.full_standard_method (averages, times1, timesback)

            partial_rollback_times.append ( partial_trollback )
            partial_standard_times.append ( partial_tstandard )

            full_rollback_times.append ( full_trollback )
            full_standard_times.append ( full_tstandard )

            print ( "Time:{0}, Slice:{1}:{2}".format ( s, s, s + 1 ) )
            print ( "PARTIAL Rollback: {0}".format ( partial_trollback ) )
            print ( "PARTIAL Standard: {0}".format ( partial_tstandard ) )
            print ( "FULL Rollback: {0}".format ( full_trollback ) )
            print ( "FULL Standard: {0}".format ( full_tstandard ) )

        run_times["Times"] = list ( range ( 0, time_slots - 1 ) )
        run_times["PartialRollback"] = partial_rollback_times
        run_times["PartialStandard"] = partial_standard_times
        run_times["FullRollback"] = full_rollback_times
        run_times["FullStandard"] = full_standard_times

        return run_times

    def partial_rollback_method(self, averages, times1, times2) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTreeRollback ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ), copy.deepcopy ( times2 ) )
        return tm / averages

    def partial_standard_method(self, averages, times1, times2) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = PartialRetroTree ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ), copy.deepcopy ( times2 ) )
        return tm / averages

    def full_rollback_method(self, averages, times1, times2) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = FullRetroTreeRollback ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ), copy.deepcopy ( times2 ) )
        return tm / averages

    def full_standard_method(self, averages, times1, times2) :
        tm = 0.0
        for i in list ( range ( averages ) ) :
            tl = FullRetroTree ()
            tm += self.base_run1 ( tl, copy.deepcopy ( times1 ), copy.deepcopy ( times2 ) )
        return tm / averages