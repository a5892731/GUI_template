from time import time
#from sys import setcheckinterval

from threading import Lock
#from multiprocessing import Lock


class ProgramInitializationBody(object):
    def __init__(self,):
        """
        We define a state object which provides some utility functions for the
        individual states within the state machine.
        """
        self.current_state = self.__class__.__name__

        self.next_state = self.__class__.__name__
        self.lock = Lock() # threading Lock mechanism

        '''
        #self.lock.acquire() # lock before read/save data
        #self.lock.release() # unlock
        '''
        self.LOOP_TIME = 0.1 # 100 ms

        self.last_loop_time = time()

        self.thread_loop_time_ms = 0 # if all is fine, then thread_loop_time_ms == LOOP_TIME


    def send_data(self):
        self.lock.acquire()  # lock before read/save data
        # GUI_data.threadTime1.set(str(self.thread_loop_time) + " [ms]")
        self.lock.release()  # unlock

    def run_state(self,states_data):
        """
        Handle events that are delegated to this State.
        """

        if (time() - self.last_loop_time) > self.LOOP_TIME:
            self.thread_loop_time_ms = round((time() - self.last_loop_time)*1000, 0)
            self.last_loop_time = time()

            self.send_data() # output stage data operations

            self.next_state = "ProgramInitialization"

        else:
            #setcheckinterval(100) # for helping GIL mechanism - optimalization in switching threads
            #https://dabeaz.com/python/UnderstandingGIL.pdf

            self.next_state = self.current_state
