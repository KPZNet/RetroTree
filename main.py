import sys
from TreeRunner import *
from RetroBSTrees import *
from PartialTreeRunner import PartialRetroTree_TestRunner

sys.setrecursionlimit(100000)

tree_runner = TreeRunner()
tree_runner.Comparison_rollback_runs()


