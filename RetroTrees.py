from BSTree import BSTree

#Intructions class holds a single action for a node
#such as "add" and "del"
class Instruction :
    def __init__(self, inst, key, payload=None) :
        self.instructionCode = inst
        self.key = key
        self.payload = payload
        if payload == None :
            self.payload = str ( key )

    #String print override
    def __str__(self) :
        s = self.instructionCode + " " + str ( self.payload ) + " key: " + str ( self.key )
        return s

#Class - List of instructions for a given time slot
class TimeSlot_Instructions :
    def __init__(self, _time) :
        self.instructions = []
        self.time = _time
        self.bst = None
    #Add additional instructions to timeslot
    def addInstruction(self, instruction) :
        self.instructions.append ( instruction )

#Class: Timeline
#Stores a full timeline of instructions that encapsulates
#a single BST.
#The Timeline class manages the life of a BST and provides all
#retroactive, current and future actions for a BST
class TimeLine :

    def __init__(self) :
        self.BST_TimeSlots = BSTree ()

    def get_timeline(self) :
        return self.BST_TimeSlots.inorder ()

    def play_instructions_on_tree(self, bst, instructions) :
        for inst in instructions :
            if inst.instructionCode == "add" :
                bst.insert ( inst.key, inst.payload )
            if inst.instructionCode == "del" :
                bst.delete ( inst.key )
        return bst

    def unplay_instructions_on_tree(self, bst, instructions) :
        for inst in instructions :
            if inst.instructionCode == "add" :
                bst.delete ( inst.key )
            if inst.instructionCode == "del" :
                bst.insert ( inst.key, inst.payload )
        return bst

    def replay_instructions_in_tree_greater_than_equal_to_time(self, tbst, time) :
        time_slots = self.get_time_slots_greater_than_equal_to_time ( time )
        for time in time_slots :
            self.play_instructions_on_tree ( tbst, time.instructions )
        return tbst

    def rollback_tree_to_time(self, bst, time) :
        tsAfter = self.get_time_slots_greater_than_equal_to_time ( time )
        tsAfter.reverse ()
        for tslot in tsAfter :
            bst = self.unplay_instructions_on_tree ( bst, tslot.instructions )
        return bst

    def get_time_slots_less_than_equal_to_time(self, time) :
        return self.BST_TimeSlots.inorderLessThanEqual ( time )

    def get_time_slots_greater_than_equal_to_time(self, time) :
        return self.BST_TimeSlots.inorderGreaterThanEqual ( time )

    def get_time_slots_greater_than_time(self, time) :
        return self.BST_TimeSlots.inorderGreaterThan ( time )

    def build_tree_from_less_than_equal_to_time(self, time) :
        tbst = BSTree ()
        time_slots = self.get_time_slots_less_than_equal_to_time ( time )
        for time in time_slots :
            self.play_instructions_on_tree ( tbst, time.instructions )
        return tbst

    def build_tree_greater_than_equal_to_time(self, time) :
        tbst = BSTree ()
        time_slots = self.get_time_slots_greater_than_equal_to_time ( time )
        for time in time_slots :
            self.play_instructions_on_tree ( tbst, time.instructions )
        return tbst

    def build_latest_tree(self) :
        bst = BSTree ()
        nds = self.BST_TimeSlots.inorder ()
        for inst in nds :
            self.play_instructions_on_tree ( bst, inst.instructions )
        return bst

    def get_tree_for_time(self, time) :
        key = self.BST_TimeSlots.get_key_for_time ( time )
        if key != -1 :
            tr = self.BST_TimeSlots.search ( key )
            pl = tr.bst
            return pl
        return None

    def print_complete_time_history(self) :
        nds = self.get_timeline ()
        for ts in nds :
            print ( "-----------------------------" )
            print ( "Time: {0}".format ( ts.time ) )
            for inst in ts.instructions :
                print ( "\t" + str ( inst ) )
            if ts.bst != None :
                ts.bst.print_tree ()
            print ( "-----------------------------" )

    def print_timeline_trees(self) :
        tl = self.BST_TimeSlots.inorder ()
        for t in tl :
            if t.bst != None :
                t.bst.print_tree ( "Time:" + str ( t.time ) )

#Represents a Partial Retroactive BST
#Partial tree allows retroactive adds/deletes
#Searches on current time only
class PartialRetroTree ( TimeLine ) :

    def __init__(self) :
        self.current_tree = BSTree ()
        super ().__init__ ()

    def Insert(self, x, time, payload=None):
        timeSlot = TimeSlot_Instructions ( time )
        timeSlot.addInstruction ( Instruction ( "add", x, payload ) )
        self.update_tree ( timeSlot )

    def Delete(self, x, time, payload=None):
        timeSlot = TimeSlot_Instructions ( time )
        timeSlot.addInstruction ( Instruction ( "del", x, payload ) )
        self.update_tree ( timeSlot )

    def get_latest_tree(self) :
        return self.current_tree

    def print_current_tree(self, str="") :
        t = self.BST_TimeSlots.getlargestkey ()
        self.current_tree.print_tree ( str + "Latest Tree time:{0}".format ( t ) )
        print ( "-----------------------------" )

    def update_tree(self, timeSlot) :
        nd = self.BST_TimeSlots.search ( timeSlot.time )
        if nd is None :
            self.BST_TimeSlots.insert ( timeSlot.time, payload=timeSlot )
        else :
            nd.instructions = (nd.instructions + timeSlot.instructions)

        latest = self.BST_TimeSlots.getlargestkey ()
        if latest != None and timeSlot.time >= latest :
            self.current_tree = self.play_instructions_on_tree ( self.current_tree, timeSlot.instructions )
        else :
            self.current_tree = self.build_latest_tree ()
        self.current_tree.rebalance ()

    def Pred(self, x) :
        return self.current_tree.search ( x )

#Partial Retroactive tree, that uses "rollback" design for
#past updates.
class PartialRetroTreeRollback ( PartialRetroTree ) :
    def __init__(self) :
        super ().__init__ ()

    def update_tree(self, timeSlot) :
        rolled_back_tree = self.rollback_tree_to_time ( self.current_tree, timeSlot.time )
        nd = self.BST_TimeSlots.search ( timeSlot.time )
        if nd is None :
            self.BST_TimeSlots.insert ( timeSlot.time, payload=timeSlot )
        else :
            nd.instructions = (nd.instructions + timeSlot.instructions)

        self.current_tree = self.replay_instructions_in_tree_greater_than_equal_to_time ( rolled_back_tree,
                                                                                          timeSlot.time )
        self.current_tree.rebalance ()

#Fully Retroactive BST
#Full retroactive supports adds/deletes and searches for any time
class FullRetroTree ( TimeLine ) :

    def __init__(self) :
        super ().__init__ ()

    def Insert(self, x, time, payload=None):
        timeSlot = TimeSlot_Instructions ( time )
        timeSlot.addInstruction ( Instruction ( "add", x, payload ) )
        self.update_tree ( timeSlot )

    def Delete(self, x, time, payload=None):
        timeSlot = TimeSlot_Instructions ( time )
        timeSlot.addInstruction ( Instruction ( "del", x, payload ) )
        self.update_tree ( timeSlot )


    def get_latest_tree(self) :
        b = self.BST_TimeSlots.get_latest_node_payload ()
        if b != None :
            return b.bst
        return BSTree ()

    def print_current_tree(self, str="") :
        pl = self.BST_TimeSlots.get_latest_node_payload ()
        pl.bst.print_tree ( str + "Latest Tree time:{0}".format ( pl.time ) )
        print ( "-----------------------------" )

    def Pred(self, x, time) :
        key = self.BST_TimeSlots.get_key_for_time ( time )
        if key != -1 :
            tr = self.BST_TimeSlots.search ( key )
            pl = tr.bst.search ( x )
            return pl
        return None

    def update_all_time_slot_tree_greater_than_equal_to_time(self, time) :
        timeSlots = self.get_time_slots_greater_than_equal_to_time ( time )
        for timeSlot in timeSlots :
            timeSlot.bst = self.build_tree_from_less_than_equal_to_time ( timeSlot.time )
            timeSlot.bst.rebalance ()

    def update_tree(self, timeSlot) :
        nd = self.BST_TimeSlots.search ( timeSlot.time )
        if nd is None :
            self.BST_TimeSlots.insert ( timeSlot.time, payload=timeSlot )
        else :
            nd.instructions = (nd.instructions + timeSlot.instructions)
        self.update_all_time_slot_tree_greater_than_equal_to_time ( timeSlot.time )
