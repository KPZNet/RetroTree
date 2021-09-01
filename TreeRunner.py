import copy
import gc
import random
import time
from datetime import datetime

import matplotlib.pyplot as plt
import pandas as pd

import config
from RetroBSTrees import Instruction, PartialRetroTreeRollback
from RetroBSTrees import PartialRetroTree
from RetroBSTrees import TimeSlot_Instructions

NANO_TO_MS = 1000000


class TreeRunner :
    def __init__(self) :
        random.seed ( datetime.now () )

    def test_tree(self) :
        tl = PartialRetroTreeRollback ()

        il = TimeSlot_Instructions ( 5 )
        il.addInstruction ( Instruction ( "add", 1 ) )
        il.addInstruction ( Instruction ( "add", 2 ) )
        il.addInstruction ( Instruction ( "add", 5 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update at 5: " )

        il = TimeSlot_Instructions ( 10 )
        il.addInstruction ( Instruction ( "add", 7 ) )
        il.addInstruction ( Instruction ( "add", 9 ) )
        il.addInstruction ( Instruction ( "add", 10 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update Time 10: " )

        il = TimeSlot_Instructions ( 20 )
        il.addInstruction ( Instruction ( "add", 16 ) )
        il.addInstruction ( Instruction ( "add", 17 ) )
        il.addInstruction ( Instruction ( "add", 20 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update Time 20: " )

        b = tl.get_rollbacked_tree_current_to_time_inclusive ( 10 )
        b.print_tree ()

        print ( "------------TIME LINE--------\n" )
        tl.print_complete_time_history ()

        print ( "------------FINAL------------\n" )
        latest = tl.get_latest_tree ()
        latest.print_tree ( "FINAL TREE" )

    def build_test_times(self, start_time, end_time, update_size, random_start, random_end) :
        timeslistAdd = []
        timeslistDel = []
        random_set = set ()
        for n in list ( range ( start_time, end_time ) ) :
            rlist = random.sample ( range ( random_start, random_end ), update_size )
            rlist = list ( set ( rlist ) )
            already_used_set = set ( random_set ).intersection ( rlist )
            randomlist = list ( set ( rlist ).symmetric_difference ( already_used_set ) )
            random_set = random_set.union ( randomlist )
            il = TimeSlot_Instructions ( n )
            ilDel = TimeSlot_Instructions ( n )
            for r in randomlist :
                il.addInstruction ( Instruction ( "add", r ) )
                ilDel.addInstruction ( Instruction ( "del", r ) )
            timeslistAdd.append ( il )
            timeslistDel.append ( ilDel )
        return timeslistAdd, timeslistDel

    def base_run1(self, tl, times1, times2) :

        for timeslot in times1 :
            tl.update_tree ( timeslot )

        config.timer_A = 0.0
        for timeslot in times2 :
            start_time = time.perf_counter_ns ()
            tl.update_tree ( timeslot )
            config.timer_A += ((time.perf_counter_ns () - start_time) / NANO_TO_MS)
        return config.timer_A

    def plot_comparison_runs(self, rts) :
        plt.plot ( rts["Times"], rts["Rollback"], label="Rollback" )
        plt.plot ( rts["Times"], rts["Standard"], label="Standard" )
        plt.title ( "Run times for Retro-BST" )
        plt.xlabel ( "Retro Update Times" )
        plt.ylabel ( "milliseconds" )
        plt.legend ()
        plt.show ()

    def Comparison_rollback_runs(self) :
        rts = self.RunUp_Back_A ()
        self.plot_comparison_runs ( rts )

    def RunUp_Back_A(self) :
        time_slots = 30
        update_size = 3
        averages = 5

        times1, times2 = self.build_test_times ( 0, time_slots, update_size, 1, 5000 )

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
