from unittest import TestCase
from RetroBSTrees import *

class TestFullRetroTree ( TestCase ) :
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
        inorder = frt.get_latest_tree().inorder()
        assert( inorder[0] == '1' and inorder[1] == '2' and inorder[2] == '3')

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

    def test_full_to_rollback(self):
        frt = FullRetroTree()
        frt.Insert ( 1, 1 )
        frt.Insert ( 2, 1 )
        frt.Insert ( 50, 100 )
        frt.Insert ( 60, 100 )
        frt.Insert ( 20, 200 )
        frt.Insert ( 30, 200 )

        frt.Delete ( 50, 150 )
        frt.Delete ( 30, 150 )
        frt.Delete ( 1, 1 )
        inorder_full = set( frt.get_latest_tree().inorder() )

        frt = FullRetroTreeRollback ()
        frt.Insert ( 1, 1 )
        frt.Insert ( 2, 1 )
        frt.Insert ( 50, 100 )
        frt.Insert ( 60, 100 )
        frt.Insert ( 20, 200 )
        frt.Insert ( 30, 200 )

        frt.Delete ( 50, 150 )
        frt.Delete ( 30, 150 )
        frt.Delete ( 1, 1 )
        inorder_rollback = set ( frt.get_latest_tree ().inorder () )

        assert inorder_full == inorder_rollback
