'''
here are the rules of state transition
'''


'''import all of states body classes'''
from resources.state_machine.machine1.states.s000_read_initialization import ReadInitializationBody
from resources.state_machine.machine1.states.s999_close_program import CloseProgramBody




class ReadInitialization(ReadInitializationBody):
    def on_event(self, states_data, GUI_data):
        '''import memory from States class'''
        self = states_data.ReadInitialization

        self.run_state(states_data, GUI_data)

        '''transition conditions'''
        if self.next_state == "ReadInitialization":
            return states_data.ReadInitialization
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class CloseProgram(CloseProgramBody):
    def on_event(self, states_data, GUI_data):
        '''import memory from States class'''
        self = states_data.CloseProgram
        '''run your functions in this state'''
        self.run_state()



