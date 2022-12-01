from threading import Lock

class State(object):
    """
    We define a state object which provides some utility functions for the
    individual states within the state machine.
    """

    def __init__(self):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.next_state = self.__class__.__name__ # name of the next state
        self.lock = Lock()  # threading Lock mechanism
        '''
        self.lock.acquire() # lock before read/save data
        self.lock.release() # unlock
        '''

    def run_state(self, states_data):
        """
        Handle events that are delegated to this State.
        """

        self.lock.acquire() # lock before read/save data
        pass
        self.lock.release() # unlock


    def __repr__(self):
        """
        Leverages the __str__ method to describe the State.
        """
        return self.__str__()

    def __str__(self):
        """
        Returns the name of the State.
        """
        return self.__class__.__name__