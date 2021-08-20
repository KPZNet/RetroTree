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
        self.BST_TimeSlots = BSTree()

    def gettimeline(self):
        return self.BST_TimeSlots.inorder()

    def Replay_TimeSlot_Instructions(self, bst, time_slot) :
        for inst in time_slot.instructions :
            if inst.instructionCode == "add" :
                bst.insert ( inst.key, inst.payload )
            if inst.instructionCode == "del" :
                bst.deleteNode ( inst.key )
        return bst

    def __sf(self, e) :
        return e.time

    def build_tree_for_time_slot(self, timeSlot, balance="False") :
        timeSlot.bst = BSTree ()
        time_slots = self.BST_TimeSlots.inorderLessThanEqual(timeSlot.time)
        for time in time_slots:
            self.Replay_TimeSlot_Instructions ( timeSlot.bst, time.payload )
        if balance :
            timeSlot.bst.rebalance ()
        return timeSlot.bst

    def RetroTimeUpdate(self, timeSlot, balance="True"):
        timeSlots = self.BST_TimeSlots.inorderGreaterThan(timeSlot.time)
        for timeSlot in timeSlots:
            self.build_tree_for_time_slot(timeSlot.payload, balance)


    def Add_TimeSlot(self, timeSlot):
        self.BST_TimeSlots.insert(timeSlot.time, payload=timeSlot)
        self.BST_TimeSlots.rebalance()
        self.build_tree_for_time_slot ( timeSlot, balance=True )
        self.RetroTimeUpdate(timeSlot)



    def build_complete_tree(self, keeptree=False, balance="False") :
        #Inorder BST builder
        bst = BSTree()
        nds = self.BST_TimeSlots.inorder()
        for inst in nds :
            self.Replay_TimeSlot_Instructions ( bst, inst.payload )
        if balance :
            bst.rebalance ()
        if keeptree :
            self.bst = bst

        return bst

    def buildtree_up_to_time(self, time, keeptree=False, balance="False") :
        bst = BSTree ()
        return bst


    def printTimeLine(self):
        nds = self.gettimeline()
        for ts in nds:
            print("Time: {0}".format(ts.payload.time))
            for inst in ts.payload.instructions:
                print("\t" + str(inst) )
