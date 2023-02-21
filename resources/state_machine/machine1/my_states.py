'''
here are the rules of state transition
'''


'''import all of states body classes'''
from resources.state_machine.machine1.states.s000_initialization import InitializationBody
from resources.state_machine.machine1.states.s999_close_program import CloseProgramBody




class Initialization(InitializationBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.Initialization

        self.run_state(states_data)

        '''transition conditions'''
        if self.next_state == "Initialization":
            return states_data.Initialization
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class CloseProgram(CloseProgramBody):
    def on_event(self, event, states_data):
        '''import memory from States class'''
        self = states_data.CloseProgram
        '''run your functions in this state'''
        self.run_state()



