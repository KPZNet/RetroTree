from NodeInstructions import FullRetroTree
from NodeInstructions import Instruction
from NodeInstructions import PartialRetroTree
from NodeInstructions import TimeSlot_Instructions
import random
from TreeRunner import TreeRunner
from PartialTreeRunner import PartialTreeRunner
import sys

print("Default Recursion Limit:")
print(sys.getrecursionlimit())
sys.setrecursionlimit(10000)
print("New Recursion Limit:")
print(sys.getrecursionlimit())

partial_tree_runner = PartialTreeRunner()
partial_tree_runner.Run1()


