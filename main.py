import sys
import matplotlib.pyplot as plt
from NodeInstructions import FullRetroTree
from PartialTreeRunner import PartialTreeRunner

sys.setrecursionlimit(100000)

def tree_run_1():
    frt = FullRetroTree()
    frt.Insert(x=10,time=1)
    frt.Insert(x=20,time=1)
    frt.Insert(x=3, time=1)
    frt.Insert(x=5, time=1)
    frt.Insert(x=9, time=1)
    frt.Insert(x=2, time=1)

    frt.print_current_tree()





tree_run_1()





