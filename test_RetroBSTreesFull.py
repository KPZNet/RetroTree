import copy
import gc
import random
import time
from datetime import datetime
from unittest import TestCase
from RetroBSTrees import *


class TestFullRetroTree ( TestCase ) :

    def build_test_slots(self, start_time, end_time, update_size, random_start, random_end) :
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

    def test_random_trees(self):
        time_slots = 10
        update_size = 250

        times1, times2 = self.build_test_slots ( 0, time_slots, update_size, 1, 5000 )

        frt = FullRetroTree()
        for tSlot in times1:
            frt.update_tree( copy.deepcopy(tSlot) )
        for delTime in times2[1:8] :
            frt.update_tree ( copy.deepcopy(delTime) )

        frtrb = FullRetroTreeRollback()
        for tSlot in times1:
            frtrb.update_tree(copy.deepcopy(tSlot))
        for delTime in times2[1:8] :
            frtrb.update_tree ( copy.deepcopy(delTime) )

        assert( set( frt.get_latest_tree().inorder() ) == set( frtrb.get_latest_tree().inorder() ) )


    def test_insert(self) :
        frt = FullRetroTree()
        frt.Insert(1,1)
        frt.Insert(2,1)
        inorder = frt.get_latest_tree().inorder()
        assert( inorder[0] == '1' and inorder[1] == '2' )

    def test_insert_over_time(self) :
        frt = FullRetroTree()
        frt.Insert(1, 100)
        frt.Insert(2, 200)
        frt.Insert ( 3, 300 )
        frt.Insert ( 4, 400 )
        frt.Insert ( 5, 500 )
        frt.Insert ( 6, 600 )

        inorder = frt.get_latest_tree().inorder()
        assert( inorder[0] == '1' and inorder[ len(inorder)- 1 ])

    def test_delete(self) :
        frt = FullRetroTree()
        frt.Insert(1, 100)
        frt.Insert(2, 100)
        frt.Insert ( 3, 100 )
        frt.Delete(2, 100 )
        frt.Delete ( 3, 100 )
        inorder = frt.get_latest_tree().inorder()
        assert( inorder[0] == '1' )

    def test_pred(self) :
        frt = FullRetroTree()
        frt.Insert ( 1, 1 )
        frt.Insert ( 2, 1 )
        frt.Insert ( 50, 100 )
        frt.Insert ( 60, 100 )
        frt.Insert ( 20, 200 )
        frt.Insert ( 30, 200 )

        n = frt.Pred(50, 110)
        assert( n == "50")

    def test_pred_not_found(self) :
        frt = FullRetroTree()
        frt.Insert ( 1, 1 )
        frt.Insert ( 2, 1 )
        frt.Insert ( 50, 100 )
        frt.Insert ( 60, 100 )
        frt.Insert ( 20, 200 )
        frt.Insert ( 30, 200 )

        n = frt.Pred(50, 99)
        assert( n == None)

    def BuildTreeTest_A(self, frt):
        frt.Insert(1, 100)
        frt.Insert(2, 200)
        frt.Insert(3, 300)
        frt.Insert(5, 500)
        frt.Insert(12, 1200)
        frt.Delete(5, 900)
        frt.Delete(3, 900)
        frt.Insert(13, 1200)
        frt.Insert(14, 1200)
        frt.Insert(15, 1500)
        frt.Insert(16, 1500)
        frt.Insert(17, 50)
        frt.Insert(18, 50)
        frt.Insert(19, 50)
        frt.Delete(13, 1200)
        frt.Delete(14, 1200)

        return frt

    def BuildTreeTest_B(self, frt):
        frt.Insert ( 1, 1 )
        frt.Insert ( 2, 1 )
        frt.Insert ( 50, 100 )
        frt.Insert ( 60, 100 )
        frt.Insert ( 20, 200 )
        frt.Insert ( 30, 200 )

        frt.Delete ( 50, 150 )
        #frt.Delete ( 30, 150 )
        #frt.Delete ( 1, 1 )
        return frt


    def test_full_to_rollback(self):
        frt = self.BuildTreeTest_A(FullRetroTree())
        frtrb = self.BuildTreeTest_A(FullRetroTreeRollback ())

        frt_tree = frt.get_latest_tree()
        frt_inorder = frt_tree.inorder()

        frtrb_tree = frtrb.get_latest_tree()
        frtrb_inorder = frtrb_tree.inorder()

        frt_inorder_set = set(frt_inorder)
        frtrb_inorder_set = set(frtrb_inorder)

        assert frt_inorder_set == frtrb_inorder_set


