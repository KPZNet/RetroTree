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

    def play_instructions_on_tree(self, bst, instructions):
        for inst in instructions:
            if inst.instructionCode == "add":
                bst.insert (inst.key, inst.payload)
            if inst.instructionCode == "del":
                bst.deleteNode (inst.key)
        return bst

    def unplay_instructions_on_tree(self, bst, instructions):
        for inst in instructions:
            if inst.instructionCode == "add":
                bst.deleteNode (inst.key)
            if inst.instructionCode == "del":
                bst.insert (inst.key, inst.payload)
        return bst

    def __sf(self, e):
        return e.time
    
    def replay_instructions_in_tree_greater_than_equal_to_time(self, tbst, time):
        time_slots = self.get_time_slots_greater_than_equal_to_time(time)
        for time in time_slots:
            self.play_instructions_on_tree (tbst, time.instructions)

        return tbst   
    
    def rollback_tree_to_time(self, bst, time):
        #get all time slots greater than time
        tsAfter = self.get_time_slots_greater_than_equal_to_time(time)
        tsAfter.reverse()
        for tslot in tsAfter:
            bst = self.unplay_instructions_on_tree(bst, tslot.instructions)
        return bst

    def get_time_slots_less_than_equal_to_time(self, time):
        return self.BST_TimeSlots.inorderLessThanEqual (time)    

    def get_time_slots_greater_than_equal_to_time(self, time):
        return self.BST_TimeSlots.inorderGreaterThanEqual (time)

    def get_time_slots_greater_than_time(self, time):
        return self.BST_TimeSlots.inorderGreaterThan (time)
    
    
    def build_tree_greater_than_equal_to_time(self, time):
        tbst = BSTree ()
        time_slots = self.get_time_slots_greater_than_equal_to_time(time)
        for time in time_slots:
            self.play_instructions_on_tree (tbst, time.instructions)

        return tbst    

    def build_latest_tree(self):
        bst = BSTree ()
        nds = self.BST_TimeSlots.inorder ()
        for inst in nds:
            self.play_instructions_on_tree (bst, inst.instructions)

        return bst

    def get_tree_for_time(self, time):
        key = self.BST_TimeSlots.get_key_for_time(time)
        if key != -1:
            tr = self.BST_TimeSlots.search(key)
            pl = tr.bst
            return pl
        return None

    def get_latest_time_slot_tree(self):
        b = self.BST_TimeSlots.get_latest_node_payload()
        if b != None:
            return b.bst
        return None

    def print_complete_time_history(self):
        nds = self.gettimeline ()
        for ts in nds:
            print ("Time: {0}".format (ts.time))
            for inst in ts.instructions:
                print ("\t" + str (inst))



class PartialRetroTree (TimeLine):
    
    def __init__(self):
        self.current_tree = BSTree()
        super().__init__()
        
    def print_current_tree(self):
        t = self.BST_TimeSlots.getlargestkey()
        self.current_tree.print_tree("Latest Tree time:{0}".format(t))      
    
    def update_tree_rollback(self, timeSlot):
        rolled_back_tree = self.rollback_tree_to_time(self.current_tree, timeSlot.time)
        rolled_back_tree.print_tree("Rollbacked Tree to time:{0}".format(timeSlot.time))
        
        nd = self.BST_TimeSlots.search(timeSlot.time)
        if nd is None:
            self.BST_TimeSlots.insert (timeSlot.time, payload=timeSlot)
        else:
            nd.instructions = (nd.instructions + timeSlot.instructions)

        self.current_tree = self.replay_instructions_in_tree_greater_than_equal_to_time(rolled_back_tree, timeSlot.time)

    def update_tree(self, timeSlot):        
        nd = self.BST_TimeSlots.search(timeSlot.time)
        if nd is None:
            self.BST_TimeSlots.insert (timeSlot.time, payload=timeSlot)
        else:
            nd.instructions = (nd.instructions + timeSlot.instructions)

        self.current_tree = self.build_latest_tree()

        
    def Pred(self, x):
        return self.current_tree.search(x)

class FullRetroTree (PartialRetroTree):
    
    def __init__(self):
        super().__init__()
        
    def print_current_tree(self):
        t = self.BST_TimeSlots.get_latest_node_payload()()
        t.bst.print_tree("Latest Tree time:{0}".format(t.time))
        
    def Pred(self, x, time):
        key = self.BST_TimeSlots.get_key_for_time(time)
        if key != -1:
            tr = self.BST_TimeSlots.search(key)
            pl = tr.bst.search(x)
            return pl
        return None

    def update_all_time_slot_tree_greater_than_time(self, time):
        timeSlots = self.get_time_slots_greater_than_time (time)
        for timeSlot in timeSlots:
            timeSlot.bst = self.build_tree_from_less_than_equal_to_time (timeSlot.time)


    def build_tree_from_less_than_equal_to_time(self, time):
        tbst = BSTree ()
        time_slots = self.get_time_slots_less_than_equal_to_time (time)
        for time in time_slots:
            self.play_instructions_on_tree (tbst, time.instructions)

        return tbst
        
    def update_tree(self, timeSlot):
        nd = self.BST_TimeSlots.search(timeSlot.time)
        if nd is None:
            self.BST_TimeSlots.insert (timeSlot.time, payload=timeSlot)
        else:
            nd.instructions = (nd.instructions + timeSlot.instructions)
    
        timeSlot.bst = self.build_tree_from_less_than_equal_to_time (timeSlot.time)
        self.update_all_time_slot_tree_greater_than_time (timeSlot.time)
        
        
        