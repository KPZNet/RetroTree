import pandas as pd
from BSTree import BSTree


class Instruction :
    def __init__(self, inst, key, payload=None) :
        self.instructionCode = inst
        self.key = key
        self.payload = payload
        if payload == None :
            self.payload = str(key)

    def __str__(self):
        s = self.instructionCode + " " + str(self.payload) + " key: " + str(self.key)
        return s


class TimeSlot_Instructions :
    def __init__(self, _time) :
        self.instructions = []
        self.time = _time
        self.bst = None

    def addInstruction(self, instruction) :
        self.instructions.append ( instruction )


class TimeLine :
    def __init__(self) :
        self.TimeSlots = []

    def Replay_TimeSlot_Instructions(self, bst, time_slot) :
        for inst in time_slot.instructions :
            if inst.instructionCode == "add" :
                bst.insert ( inst.key, inst.payload )
            if inst.instructionCode == "del" :
                bst.deleteNode ( inst.key )
        return bst

    def __sf(self, e) :
        return e.time

    def build_tree_for_time_slot(self, inst, balance="False") :
        inst.bst = BSTree ()
        self.Replay_TimeSlot_Instructions ( inst.bst, inst )
        if balance :
            inst.bst.rebalance ()
        return inst.bst

    def Add_TimeSlot(self, inst) :
        self.build_tree_for_time_slot(inst, balance=True)
        self.TimeSlots.append ( inst )
        self.TimeSlots.sort ( key=self._TimeLine__sf )

    def build_complete_tree(self, keeptree=False, balance="False") :
        bst = BSTree ()
        for inst in self.TimeSlots :
            self.Replay_TimeSlot_Instructions ( bst, inst )
        if balance :
            bst.rebalance ()
        if keeptree :
            self.bst = bst
        return bst

    def buildtree_up_to_time(self, time, keeptree=False, balance="False") :
        bst = BSTree ()
        for inst in self.TimeSlots :
            if inst.time <= time :
                self.Replay_TimeSlot_Instructions ( bst, inst )
        if balance :
            bst.rebalance ()
        if keeptree :
            self.bst = bst
        return bst

    def printTimeLine(self):
        for ts in self.TimeSlots:
            print("Time: {0}".format(ts.time))
            for inst in ts.instructions:
                print("\t" + str(inst) )


