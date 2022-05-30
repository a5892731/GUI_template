from tkinter import *
'''------------------------------------------------------------------------------------------------------------------'''
def window_variables_init(self):
    def gui_mechanism_variables():
        self.window_width = 0
        self.window_height = 0
        self.tab_name = ""

    def support_variables():
        self.int_var_type = IntVar()
        self.string_var_type = StringVar()

    def side_1_variables():
        self.int_var_type_1 = IntVar()
        self.int_var_type_2 = IntVar()
        self.int_var_type_3 = IntVar()
        self.int_var_type_4 = IntVar()
        self.int_var_type_5 = IntVar()
        self.string_var_type = StringVar()

    #----------------------------------------------------------------------
    gui_mechanism_variables()
    side_1_variables()


'''------------------------------------------------------------------------------------------------------------------'''
def set_variable_default_values(self):
    def gui_mechanism_variables():
        self.window_width = self.window.winfo_screenwidth()
        self.window_height = self.window.winfo_screenheight() - 30
        self.tab_name = "Terminal"
    def udp_variables():
        self.receive_string = ""



    #----------------------------------------------------------------------
    gui_mechanism_variables()
    udp_variables()


def import_variables_to_gui(self, state_machine_variables):
    '''this function is prepared to import data to gui from state machine'''

    def terminal(state_machine_variables):
        pass


    #----------------------------------------------------------------------
    if self.tab_name == "Terminal":
        terminal(state_machine_variables)

def export_variables_from_gui(self, state_machine_variables):
    '''this function is prepared to export data from gui to state machine'''
    def terminal(state_machine_variables):
        pass

        #----------------------------------------------------------------------
    if self.tab_name == "Terminal":
        terminal(state_machine_variables)