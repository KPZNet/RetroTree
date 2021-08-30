import random
import time
from datetime import datetime

import config
from RetroBSTrees import Instruction
from RetroBSTrees import PartialRetroTree
from RetroBSTrees import TimeSlot_Instructions

NANO_TO_MS = 1000000


class TreeRunner :
    def __init__(self) :
        random.seed ( datetime.now () )

    def test_tree(self) :
        tl = PartialRetroTree ()

        il = TimeSlot_Instructions ( 5 )
        il.addInstruction ( Instruction ( "add", 40 ) )
        il.addInstruction ( Instruction ( "add", 150 ) )
        il.addInstruction ( Instruction ( "add", 160 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update at 5: " )

        il = TimeSlot_Instructions ( 10 )
        il.addInstruction ( Instruction ( "add", 39 ) )
        il.addInstruction ( Instruction ( "add", 20 ) )
        il.addInstruction ( Instruction ( "add", 70 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update Time 10: " )

        il = TimeSlot_Instructions ( 20 )
        il.addInstruction ( Instruction ( "add", 67 ) )
        il.addInstruction ( Instruction ( "add", 26 ) )
        il.addInstruction ( Instruction ( "add", 33 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update Time 20: " )

        il = TimeSlot_Instructions ( 15 )
        il.addInstruction ( Instruction ( "del", 20 ) )
        tl.update_tree ( il )
        tl.print_current_tree ( "Update Time 15: " )

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
