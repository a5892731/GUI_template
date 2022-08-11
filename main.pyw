# author: a5892731
# date: 11.05.2022
# last update: 29.07.2022
# version: 1.3
#
# description:
# This is a simple template for programs with Graphic User Interface

'''
imports
-tkinter: pip install tk
-PIL: pip install pillow
'''

from tkinter import Tk
from threading import Thread, Lock

from resources.state_machine.state_loader import StateLoader


class ProgramRun:
    from resources.gui._gui_variables import window_variables_init, set_variable_default_values
    from resources.gui._gui_variables_updater import import_variables_to_gui, export_variables_from_gui
    from resources.gui._main_window import build_main_window, update_window

    '''>>> imports used in other files connected to this class'''
    from resources.gui.windows._left_menu_label import _left_menu_bar, exit_program, view_side_1_label
    from resources.gui.windows._side_1_label import _side_1_label




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
            '''create threads'''
            threads = []
            self.update_window()


            thread = Thread(
                target=device.on_event(self, 'device_locked',)
            )
            threads.append(thread)





            '''start threads'''
            for thread in threads:
                thread.start()

            '''wait for all threads to end'''
            for thread in threads:
                thread.join()

            try:
                self.window.winfo_exists()  # if there is no window then exit program
            except:
                exit()




'''---------------------------------------START APP------------------------------------------------------------------'''
app = ProgramRun()