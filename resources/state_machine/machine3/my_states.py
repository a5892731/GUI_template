'''
here are the rules of state transition
'''


'''import all of states body classes'''
from resources.state_machine.machine3.states.s000_send_initialization import SendInitializationBody
from resources.state_machine.machine3.states.s999_close_program import CloseProgramBody




class SendInitialization(SendInitializationBody):
    def on_event(self, states_data, GUI_data):
        '''import memory from States class'''
        self = states_data.SendInitialization

        self.run_state(states_data, GUI_data)

        '''transition conditions'''
        if self.next_state == "SendInitialization":
            return states_data.SendInitialization
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class CloseProgram(CloseProgramBody):
    def on_event(self, states_data, GUI_data):
        '''import memory from States class'''
        self = states_data.CloseProgram
        '''run your functions in this state'''
        self.run_state()



