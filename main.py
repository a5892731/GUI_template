# author: a5892731
# date: 11.05.2022
# last update: 12.05.2022
# version: 1.0.1
#
# description:
# This is a simple template for programs with Graphic User Interface

from tkinter import *

class ProgramRun:
    from resources.gui._gui_variables import window_variables_init, set_variable_default_values
    from resources.gui._main_window import build_main_window, update_window
    from resources.gui.labels._left_menu_label import left_menu_bar, exit_program, view_side_1, view_side_2
    from resources.gui.labels._side_1 import side_1_label
    from resources.gui.labels._side_2 import side_2_label

    def __init__(self,):
        self.window = Tk()
        self.window_variables_init()
        self.set_variable_default_values()
        self.build_main_window()

        self.main_loop()

    def main_loop(self):
        while True:
            self.update_window()

            self.execute_test_program_tasks()


    def execute_test_program_tasks(self):
        pass


'''---------------------------------------START APP------------------------------------------------------------------'''
app = ProgramRun()