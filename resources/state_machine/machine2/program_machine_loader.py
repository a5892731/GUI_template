'''Sources:

https://gist.github.com/Karn/8fac5d8cc31a9a6b1e2bfb31e2a4267b
'''

from threading import Lock

class ProgramMachine(object):
    """
    A simple state machine that mimics the functionality of a device from a
    high level.
    """

    def __init__(self, states_data, gui_data):
        """ Initialize the components. """
        # Initialize all states for memory storage purposes
        self.states_data = states_data
        self.gui_data = gui_data
        # Select an initial state
        self.state = self.states_data.ProgramInitialization

        self.lock = Lock()  # threading Lock mechanism
        '''
        self.lock.acquire() # lock before read/save data
        self.lock.release() # unlock
        '''


    def on_event(self):
        """
        This is the bread and butter of the state machine. Incoming events are
        delegated to the given states which then handle the event. The result is
        then assigned as the new state.
        """
        # Save down the name of the currently called state
        self.states_data.current_state = self.state.__class__.__name__

        # The next state will be the result of the on_event function.
        self.state = self.state.on_event(states_data=self.states_data, GUI_data = self.gui_data)

