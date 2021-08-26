from TreeRunner import TreeRunner
from NodeInstructions import FullRetroTree
from NodeInstructions import Instruction
from NodeInstructions import PartialRetroTree
from NodeInstructions import TimeSlot_Instructions
import random

class PartialTreeRunner(TreeRunner):
    def __init__(self) :
        super ().__init__ ()

    def Run1(self):
        tl = PartialRetroTree()
        self.base_run1(tl)
