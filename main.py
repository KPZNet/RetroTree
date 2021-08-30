import sys
import matplotlib.pyplot as plt
from RetroTrees import FullRetroTree
from PartialTreeRunner import PartialRetroTree_TestRunner

sys.setrecursionlimit(100000)

pt_runner = PartialRetroTree_TestRunner()
pt_runner.Comparison_rollback_runs()

