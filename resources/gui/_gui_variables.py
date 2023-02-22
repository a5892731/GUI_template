from tkinter import IntVar, StringVar
'''------------------------------------------------------------------------------------------------------------------'''
def window_variables_init(self):
    def gui_mechanism_variables():
        self.window_width = 0
        self.window_height = 0
        self.tab_name = ""

    def support_variables():
        self.int_var_type = IntVar()
        self.string_var_type = StringVar()

    def program_performance_variables():
        self.threat1_ms = StringVar()
        self.threat2_ms = StringVar()
        self.threat3_ms = StringVar()


    #----------------------------------------------------------------------
    gui_mechanism_variables()
    program_performance_variables()

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
