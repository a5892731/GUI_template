'''Sources:

https://gist.github.com/Karn/8fac5d8cc31a9a6b1e2bfb31e2a4267b
'''

from threading import Lock

class SendUDPmachine(object):
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
        self.state = self.states_data.SendInitialization

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
        self.lock.acquire() # lock before read/save data
        self.states_data.current_state_UDP = self.state.__class__.__name__
        self.lock.release()  # unlock

        # The next state will be the result of the on_event function.
        self.gui_data.semaphore.acquire()

        number_of_states = 2
        state_number = 0

        while state_number != number_of_states:
            state_number += 1
            self.state = self.state.on_event(states_data=self.states_data, GUI_data = self.gui_data)

        self.gui_data.semaphore.release()