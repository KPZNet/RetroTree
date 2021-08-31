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

    def test_get_latest_tree(self) :
        self.fail ()

    def test_print_current_tree(self) :
        self.fail ()

    def test_pred(self) :
        self.fail ()

    def test_update_all_time_slot_tree_greater_than_equal_to_time(self) :
        self.fail ()

    def test_update_tree(self) :
        self.fail ()
