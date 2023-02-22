# author: a5892731
# date: 11.05.2022
# last update: 21.02.2023
# version: 1.4
#
# description:
# This is a simple template for programs with Graphic User Interface

'''
imports
-tkinter: pip install tk
-PIL: pip install pillow
'''

from tkinter import Tk
from threading import Thread, BoundedSemaphore

'''init states machine'''
from resources.state_machine.machine1.read_machine_loader import ReadUDPmachine
from resources.state_machine.machine2.program_machine_loader import ProgramMachine
from resources.state_machine.machine3.send_machine_loader import SendUDPmachine

'''init data buffer'''
from resources.state_machine.states_data_buffer import StatesDataBuffer


class ProgramRun:
    from resources.gui._gui_variables import window_variables_init, set_variable_default_values
    from resources.gui._main_window import build_main_window, update_window

    '''>>> imports used in other files connected to this class'''
    from resources.gui.windows._left_menu_label import _left_menu_bar, exit_program
    from resources.gui.windows._home_label import _home_label
    from resources.gui.windows._settings_label import _settings_label

    '''<<< imports used in other files connected to this class'''
    def __init__(self,):
        self.window = Tk()
        self.window_variables_init()
        self.set_variable_default_values()
        self.build_main_window()

        self.semaphore = BoundedSemaphore(value = 2)

        # Initialize all states for memory storage purposes
        self.states_data = StatesDataBuffer()

        self.main_loop()

    def main_loop(self):

        read_machine = ReadUDPmachine(states_data=self.states_data, gui_data=self)
        program_machine = ProgramMachine(states_data=self.states_data, gui_data=self)
        send_machine = SendUDPmachine(states_data=self.states_data, gui_data=self)


        while True:
            '''create threads'''
            threads = []
            self.update_window()


            thread = Thread(
                target=read_machine.on_event()
            )
            threads.append(thread)

            thread = Thread(
                target=program_machine.on_event()
            )
            threads.append(thread)

            thread = Thread(
                target=send_machine.on_event()
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