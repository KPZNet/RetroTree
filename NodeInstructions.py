from BSTree import BSTree


class Instruction:

    def __init__(self, inst, key, payload=None):
        self.instructionCode = inst
        self.key = key
        self.payload = payload
        if payload == None:
            self.payload = str (key)

    def __str__(self):
        s = self.instructionCode + " " + str (self.payload) + " key: " + str (self.key)
        return s


class TimeSlot_Instructions:

    def __init__(self, _time):
        self.instructions = []
        self.time = _time
        self.bst = None

    def addInstruction(self, instruction):
        self.instructions.append (instruction)


class TimeLine:

    def __init__(self):
        self.BST_TimeSlots = BSTree ()

    def gettimeline(self):
        return self.BST_TimeSlots.inorder ()

    def Replay_TimeSlot_Instructions(self, bst, instructions):
        for inst in instructions:
            if inst.instructionCode == "add":
                bst.insert (inst.key, inst.payload)
            if inst.instructionCode == "del":
                bst.deleteNode (inst.key)
        return bst

    def __sf(self, e):
        return e.time


    def get_time_slots_up_to_time(self, time):
        return self.BST_TimeSlots.inorderLessThanEqual (time)

    def get_time_slots_greater_equal_to_time(self, time):
        return self.BST_TimeSlots.inorderGreaterThanEqual (time)

    def get_time_slots_after_time(self, time):
        return self.BST_TimeSlots.inorderGreaterThan (time)

    def build_tree_up_to_time(self, time):
        tbst = BSTree ()
        time_slots = self.get_time_slots_up_to_time (time)
        for time in time_slots:
            self.Replay_TimeSlot_Instructions (tbst, time.instructions)

        tbst.rebalance ()
        return tbst

    def build_tree_after_time(self, time, balance="True"):
        tbst = BSTree ()
        time_slots = self.BST_TimeSlots.inorderGreaterThan (time)
        for time in time_slots:
            self.Replay_TimeSlot_Instructions (tbst, time.instructions)
        if balance:
            tbst.rebalance ()
        return tbst

    def build_all_trees_after_time(self, time):
        timeSlots = self.get_time_slots_after_time (time)
        for timeSlot in timeSlots:
            timeSlot.bst = self.build_tree_up_to_time (timeSlot.time)

    def Pred(self, x, time):
        key = self.BST_TimeSlots.get_key_for_time(time)
        if key != -1:
            tr = self.BST_TimeSlots.search(key)
            pl = tr.bst.search(x)
            return pl
        return None

    def get_tree_for_time(self, time):
        key = self.BST_TimeSlots.get_key_for_time(time)
        if key != -1:
            tr = self.BST_TimeSlots.search(key)
            pl = tr.bst
            return pl
        return None

    def UpdateTree(self, timeSlot):
        nd = self.BST_TimeSlots.search(timeSlot.time)
        if nd is None:
            self.BST_TimeSlots.insert (timeSlot.time, payload=timeSlot)
        else:
            nd.instructions = (nd.instructions + timeSlot.instructions)

        self.BST_TimeSlots.rebalance ()

        timeSlot.bst = self.build_tree_up_to_time (timeSlot.time)
        self.build_all_trees_after_time (timeSlot.time)

    def build_complete_tree(self):
        # Inorder BST builder
        bst = BSTree ()
        nds = self.BST_TimeSlots.inorder ()
        for inst in nds:
            self.Replay_TimeSlot_Instructions (bst, inst.instructions)

        bst.rebalance ()
        return bst

    def printTimeLine(self):
        nds = self.gettimeline ()
        for ts in nds:
            print ("Time: {0}".format (ts.time))
            for inst in ts.instructions:
                print ("\t" + str (inst))

    def getlatesttree(self):
       b = self.BST_TimeSlots.getlargestpayload()
       if b != None:
           return b.bst
       return None

