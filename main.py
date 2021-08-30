import sys
import matplotlib.pyplot as plt
from RetroBSTrees import FullRetroTree
from PartialTreeRunner import PartialTreeRunner

sys.setrecursionlimit(100000)

pt_runner = PartialTreeRunner()
pt_runner.Comparison_rollback_runs()

