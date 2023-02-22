#from threading import Lock
from multiprocessing import Lock

class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.next_state = self.__class__.__name__
        self.lock = Lock() # threading Lock mechanism
        '''
        self.lock.acquire() # lock before read/save data
        self.lock.release() # unlock
        '''

        self.init_variables()

    def init_variables(self):
        pass

    def get_data(self, states_data, GUI_data):
        self.lock.acquire()
        pass
        self.lock.release()

    def send_data(self, states_data, GUI_data):
        self.lock.acquire()
        pass
        self.lock.release()

    def run_state(self,  states_data, GUI_data):
        """
        Handle events that are delegated to this State.
        """
        self.get_data(states_data, GUI_data)

        pass

        self.send_data(states_data, GUI_data)


        self.next_state = "statename"


