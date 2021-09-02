from unittest import TestCase
from RetroBSTrees import *


class TestPartialRetroTree ( TestCase ) :
    def test_insert(self) :
        frt = PartialRetroTree()
        frt.Insert(1,1)
        frt.Insert(2,1)
        inorder = frt.get_latest_tree().inorder()
        assert( inorder[0] == '1' and inorder[1] == '2' )

