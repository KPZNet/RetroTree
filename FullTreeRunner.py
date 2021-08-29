from TreeRunner import TreeRunner
from RetroTrees import FullRetroTree
from RetroTrees import Instruction
from RetroTrees import PartialRetroTree
from RetroTrees import TimeSlot_Instructions
import random

class FullTreeRunner(TreeRunner):
    def __init__(self) :
        super ().__init__ ()

    def Run1(self):
        tl = FullRetroTree()
        self.base_run1(tl)
