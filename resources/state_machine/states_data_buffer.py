'''import all your states here'''
from resources.state_machine.my_states import Initialization, CloseProgram

class StatesDataBuffer():
    def __init__(self):
        '''information variables'''
        self.current_state = None
        self.info = "info"


        '''init all your states here
        this class stores memory of States'''
        self.Initialization = Initialization()
        self.CloseProgram = CloseProgram()