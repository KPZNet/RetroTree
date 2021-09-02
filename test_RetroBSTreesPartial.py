from unittest import TestCase
from RetroBSTrees import *


class TestPartialRetroTree ( TestCase ) :
    def test_insert(self) :
        frt = PartialRetroTree()
        frt.Insert(1,1)
        frt.Insert(2,1)
        inorder = frt.get_latest_tree().inorder()
        assert( inorder[0] == '1' and inorder[1] == '2' )

    def test_delete(self) :
        frt = PartialRetroTree()
        frt.Insert(1, 100)
        frt.Insert(2, 100)
        frt.Insert ( 3, 100 )
        frt.Delete(2, 100 )
        frt.Delete ( 3, 100 )
        inorder = frt.get_latest_tree().inorder()
        assert( inorder[0] == '1' )

    def test_pred(self) :
        frt = PartialRetroTree()
        frt.Insert ( 1, 1 )
        frt.Insert ( 2, 1 )
        frt.Insert ( 50, 100 )
        frt.Insert ( 60, 100 )
        frt.Insert ( 20, 200 )
        frt.Insert ( 30, 200 )

        n = frt.Pred(50)
        assert( n == "50")