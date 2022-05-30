# author: a5892731
# date: 11.05.2022
# last update: 30.05.2022
# version: 1.1
#
# description:
# This is a simple template for programs with Graphic User Interface

'''
imports
-tkinter: pip install tk
-PIL: pip install pillow
'''

from tkinter import Tk
from time import time

from resources.state_machine.state_loader import StateLoader


class ProgramRun:
    from resources.gui._gui_variables import window_variables_init, set_variable_default_values, \
                                             import_variables_to_gui, export_variables_from_gui
    from resources.gui._main_window import build_main_window, update_window

    '''>>> imports used in other files connected to this class'''
    from resources.gui.labels._left_menu_label import left_menu_bar, exit_program, view_side_1_label
    from resources.gui.labels._side_1_label import side_1_label




    '''<<< imports used in other files connected to this class'''
    def __init__(self,):
        self.window = Tk()
        self.window_variables_init()
        self.set_variable_default_values()
        self.build_main_window()

        self.main_loop()

    def main_loop(self):
        device = StateLoader()

        while True:
            #start_time = time()
            self.update_window()

            device.on_event(self, 'device_locked',)  # call the state machine events

            #loop_time = time() - start_time
            #print(">>> main loop time = {}".format(loop_time))





'''---------------------------------------START APP------------------------------------------------------------------'''
app = ProgramRun()