#!/usr/bin/env python
#
##############################################################################
# Imports
##############################################################################
import py_trees

# set global enviornments
RH = True
PH = True
Conscious = False
Bleeding = True
Breathing = True
Pulse = False
##############################################################################
# Classes
##############################################################################
# Condition 1: check rescuer hazard
class CheckRH(py_trees.behaviour.Behaviour):
    def __init__(self, name = 'Check_Resucuer_Hazard'):
        super(CheckRH, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, timeout):
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
       # self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        pass

    def update(self):
        global RH
        new_status = py_trees.Status.SUCCESS if RH else py_trees.Status.FAILURE
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "Rescuer Hazard!"
        elif new_status == py_trees.Status.FAILURE:
            self.feedback_message = "RH Clear"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status


    def terminate(self, new_status):
     #   self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass
        
# Condition 2: check patient hazard
class CheckPH(py_trees.behaviour.Behaviour):
    def __init__(self, name = 'Check_Patient_Hazard'):
        super(CheckPH, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, timeout):
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
    #    self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        pass

    def update(self):
        global PH
        new_status = py_trees.Status.SUCCESS if PH else py_trees.Status.FAILURE
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "Patient Hazard!"
        elif new_status == py_trees.Status.FAILURE:
            self.feedback_message = "PH Clear"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status


    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass
        
# Condition 3: check conciousness
class CheckConscious(py_trees.behaviour.Behaviour):
    def __init__(self, name = 'Check_Consciousness'):
        super(CheckConscious, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, timeout):
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
   #     self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        pass

    def update(self):
        global Concious
        new_status = py_trees.Status.SUCCESS if Conscious else py_trees.Status.FAILURE
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "Patient is conscious"
        elif new_status == py_trees.Status.FAILURE:
            self.feedback_message = "Patient is unconscious!"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status


    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass
        
# Condition 4: check breathing
class CheckBreath(py_trees.behaviour.Behaviour):
    def __init__(self, name = 'Check_Breathing'):
        super(CheckBreath, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, timeout):
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
   #     self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        pass

    def update(self):
        global Breathing
        new_status = py_trees.Status.SUCCESS if Breathing else py_trees.Status.FAILURE
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "Patient is breathing"
        elif new_status == py_trees.Status.FAILURE:
            self.feedback_message = "Patient is not breathing!"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status


    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass

# Condition 5: check pulse
class CheckPulse(py_trees.behaviour.Behaviour):
    def __init__(self, name = 'Check_Pulse'):
        super(CheckPulse, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, timeout):
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
   #     self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        pass

    def update(self):
        global Pulse
        new_status = py_trees.Status.SUCCESS if Pulse else py_trees.Status.FAILURE
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "Patient has pulse"
        elif new_status == py_trees.Status.FAILURE:
            self.feedback_message = "Patient has no pulse!"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status


    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass
        
# Condition 6: check bleeding
class CheckBleed(py_trees.behaviour.Behaviour):
    def __init__(self, name = 'Check_Bleeding'):
        super(CheckBleed, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, timeout):
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
   #     self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        pass

    def update(self):
        global Bleeding
        new_status = py_trees.Status.SUCCESS if Bleeding else py_trees.Status.FAILURE
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "Patient is bleeding!"
        elif new_status == py_trees.Status.FAILURE:
            self.feedback_message = "Patient is not bleeding"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status


    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass

# Action 1: Eliminate Rescuer Hazard
class EliminateResHazard(py_trees.behaviour.Behaviour):
    def __init__(self, name="Eliminate_Hazard"):
        """
        Default construction.
        """
        super(EliminateResHazard, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, unused_timeout=15):
        """
        No delayed initialisation required for this example.
        """
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
        """
        Reset a counter variable.
        """
       # self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        self.counter = 0

    def update(self):
        global RH
        """
        Increment the counter and decide upon a new status result for the behaviour.
        """
        self.counter += 1
        new_status = py_trees.Status.SUCCESS if self.counter == 3 else py_trees.Status.RUNNING
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "hazard eliminated".format(self.counter)
            RH = False
        else:
            self.feedback_message = "still eliminating"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status

    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass

# Action 2: Eliminate Patient Hazard
class EliminatePatHazard(py_trees.behaviour.Behaviour):
    def __init__(self, name="Eliminate_Hazard"):
        """
        Default construction.
        """
        super(EliminatePatHazard, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, unused_timeout=15):
        """
        No delayed initialisation required for this example.
        """
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
        """
        Reset a counter variable.
        """
       # self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        self.counter = 0

    def update(self):
        global PH
        """
        Increment the counter and decide upon a new status result for the behaviour.
        """
        self.counter += 1
        new_status = py_trees.Status.SUCCESS if self.counter == 3 else py_trees.Status.RUNNING
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "hazard eliminated".format(self.counter)
            PH = False
        else:
            self.feedback_message = "still eliminating"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status

    def terminate(self, new_status):
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass

# Action 3: Control Bleeding
class ControlBleed(py_trees.behaviour.Behaviour):
    def __init__(self, name="Control_Bleeding"):
        """
        Default construction.
        """
        super(ControlBleed, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, unused_timeout=15):
        """
        No delayed initialisation required for this example.
        """
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
        """
        Reset a counter variable.
        """
      #  self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        self.counter = 0

    def update(self):
        global Bleeding
        """
        Increment the counter and decide upon a new status result for the behaviour.
        """
        self.counter += 1
        new_status = py_trees.Status.SUCCESS if self.counter == 3 else py_trees.Status.RUNNING
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "Bleeding Controlled".format(self.counter)
            Bleeding = False
        else:
            self.feedback_message = "Controlling Bleeding"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status

    def terminate(self, new_status):
        """
        Nothing to clean up in this example.
        """
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass

# Action 4: Open Airway
class OpenAirway(py_trees.behaviour.Behaviour):
    def __init__(self, name="Open_Airway"):
        """
        Default construction.
        """
        super(OpenAirway, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, unused_timeout=15):
        """
        No delayed initialisation required for this example.
        """
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
        """
        Reset a counter variable.
        """
      #  self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        self.counter = 0

    def update(self):
        """
        Increment the counter and decide upon a new status result for the behaviour.
        """
        self.counter += 1
        new_status = py_trees.Status.SUCCESS if self.counter == 3 else py_trees.Status.RUNNING
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "airway opened".format(self.counter)
        else:
            self.feedback_message = "openning airway"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status

    def terminate(self, new_status):
        """
        Nothing to clean up in this example.
        """
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass
                 
# Action 5: Artificial ventilation
class ArtiVenti(py_trees.behaviour.Behaviour):
    def __init__(self, name="Artificial_Ventilation"):
        """
        Default construction.
        """
        super(ArtiVenti, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, unused_timeout=15):
        """
        No delayed initialisation required for this example.
        """
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
        """
        Reset a counter variable.
        """
     #   self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        self.counter = 0

    def update(self):
        """
        Increment the counter and decide upon a new status result for the behaviour.
        """
        global Breathing
        self.counter += 1
        new_status = py_trees.Status.SUCCESS if self.counter == 3 else py_trees.Status.RUNNING
        if new_status == py_trees.Status.SUCCESS:
            Breathing = True
            self.feedback_message = "artificial ventilation done".format(self.counter)
        else:
            self.feedback_message = "still performing artificial ventilation"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status

    def terminate(self, new_status):
        """
        Nothing to clean up in this example.
        """
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass

# Action 6: External Cardic Compression
class ExCardCompr(py_trees.behaviour.Behaviour):
    def __init__(self, name="External_Cardic_Compression"):
        """
        Default construction.
        """
        super(ExCardCompr, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, unused_timeout=15):
        """
        No delayed initialisation required for this example.
        """
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
        """
        Reset a counter variable.
        """
      #  self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        self.counter = 0

    def update(self):
        global Pulse
        """
        Increment the counter and decide upon a new status result for the behaviour.
        """
        self.counter += 1
        new_status = py_trees.Status.SUCCESS if self.counter == 3 else py_trees.Status.RUNNING
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "External Cardic Compression done".format(self.counter)
            Pulse = True
        else:
            self.feedback_message = "still performing External Cardic Compression"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status

    def terminate(self, new_status):
        """
        Nothing to clean up in this example.
        """
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass
        
# Action 7: Secondary Survey
class SecSurvey(py_trees.behaviour.Behaviour):
    def __init__(self, name="Secondary_Survey"):
        """
        Default construction.
        """
        super(SecSurvey, self).__init__(name)
        self.logger.debug("%s.__init__()" % (self.__class__.__name__))

    def setup(self, unused_timeout=15):
        """
        No delayed initialisation required for this example.
        """
        self.logger.debug("%s.setup()" % (self.__class__.__name__))
        return True

    def initialise(self):
        """
        Reset a counter variable.
        """
      #  self.logger.debug("%s.initialise()]" % (self.__class__.__name__))
        self.counter = 0

    def update(self):
        """
        Increment the counter and decide upon a new status result for the behaviour.
        """
        self.counter += 1
        new_status = py_trees.Status.SUCCESS if self.counter == 3 else py_trees.Status.RUNNING
        if new_status == py_trees.Status.SUCCESS:
            self.feedback_message = "Secondary Survey done".format(self.counter)
        else:
            self.feedback_message = "still performing Secondary Survey"
        self.logger.debug("%s.update()[%s->%s][%s]" % (self.__class__.__name__, self.status, new_status, self.feedback_message))
        return new_status

    def terminate(self, new_status):
        """
        Nothing to clean up in this example.
        """
        self.logger.debug("%s.terminate()[%s->%s]" % (self.__class__.__name__, self.status, new_status))
        pass

##############################################################################
# Main
##############################################################################
def main():
    
    # composites
    root = py_trees.composites.Selector("Rescuer_Hazard?")
    sequence1 = py_trees.composites.Sequence("Rescuer_Hazard!")
    condition2 = py_trees.composites.Selector("Patient_Hazard?")
    sequence2 = py_trees.composites.Sequence("Patient_Hazard!")
    condition3 = py_trees.composites.Selector("Conscious?")
    sequence3 = py_trees.composites.Sequence("Conscious!")
    condition4 = py_trees.composites.Selector("Breath?")
    sequence4 = py_trees.composites.Sequence("Breath!")
    condition5_1 = py_trees.composites.Selector("ConsBleeding?")
    condition5_2 = py_trees.composites.Selector("UncoBleeding?")
    sequence5_1 = py_trees.composites.Sequence("ConsBleeding!")
    sequence5_2 = py_trees.composites.Sequence("UncoBleeding!")
    condition6 = py_trees.composites.Selector("Pulse?")
    sequence6 = py_trees.composites.Sequence("Pulse!")
    sequence7 = py_trees.composites.Sequence("Unconscious!")

    # conditions
    CRH = CheckRH()
    CPH = CheckPH()
    CC = CheckConscious()
    CBL_1 = CheckBleed()
    CBL_2 = CheckBleed()
    CB = CheckBreath()
    CP = CheckPulse()

    # actions
    ERH = EliminateResHazard()
    EPH = EliminatePatHazard()
    CtrlB_1 = ControlBleed()
    CtrlB_2 = ControlBleed()
    OA = OpenAirway()
    AV = ArtiVenti()
    ECC = ExCardCompr()
    SS_Cons = SecSurvey()
    SS_Unco = SecSurvey()

    # build tree
    sequence1.add_children([CRH,ERH])
    sequence2.add_children([CPH,EPH])
    sequence3.add_children([CC,condition5_1])
    sequence4.add_children([CB,condition6])
    sequence5_1.add_children([CBL_1,CtrlB_1])
    sequence5_2.add_children([CBL_2,CtrlB_2])
    sequence6.add_children([CP,condition5_2])
    sequence7.add_children([OA,condition4])
    root.add_children([sequence1,condition2])
    condition2.add_children([sequence2,condition3])
    condition3.add_children([sequence3,sequence7])
    condition4.add_children([sequence4,AV])
    condition5_1.add_children([sequence5_1,SS_Cons])
    condition5_2.add_children([sequence5_2,SS_Unco])
    condition6.add_children([sequence6,ECC])
    behaviour_tree = py_trees.trees.BehaviourTree(root)
    behaviour_tree.visitors.append(py_trees.visitors.DebugVisitor())
    snapshot_visitor = py_trees.visitors.SnapshotVisitor()
    behaviour_tree.visitors.append(snapshot_visitor)
    behaviour_tree.setup(15)
    try:
        """
        py_trees.logging.level = py_trees.logging.Level.DEBUG
        behaviour_tree.tick_tock(
                sleep_ms=500,
                number_of_iterations=py_trees.trees.CONTINUOUS_TICK_TOCK,
                pre_tick_handler=None,
                post_tick_handler=None
            )
        """
        for i in range(30):
            behaviour_tree.tick()
            ascii_tree = py_trees.display.ascii_tree(
                behaviour_tree.root,
                snapshot_information=snapshot_visitor)
            print(ascii_tree)
        
    except KeyboardInterrupt:
        behaviour_tree.interrupt()
    
if __name__ == '__main__':
    main()