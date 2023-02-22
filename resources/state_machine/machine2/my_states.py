'''
here are the rules of state transition
'''


'''import all of states body classes'''
from resources.state_machine.machine2.states.s000_program_loop_initialization import ProgramInitializationBody
from resources.state_machine.machine2.states.s999_close_program import CloseProgramBody




class ProgramInitialization(ProgramInitializationBody):
    def on_event(self, states_data, GUI_data):
        '''import memory from States class'''
        self = states_data.ProgramInitialization

        self.run_state(states_data)

        '''transition conditions'''
        if self.next_state == "ProgramInitialization":
            return states_data.ProgramInitialization
        else:
            states_data.CloseProgram.info = ">>> Info: transition error in {} state".format(self)
            return states_data.CloseProgram

class CloseProgram(CloseProgramBody):
    def on_event(self, states_data, GUI_data):
        '''import memory from States class'''
        self = states_data.CloseProgram
        '''run your functions in this state'''
        self.run_state()



