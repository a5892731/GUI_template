from tkinter import *
'''------------------------------------------------------------------------------------------------------------------'''
def window_variables_init(self):
    def gui_mechanism_variables():
        self.window_width = self.window.winfo_screenwidth()
        self.window_height = self.window.winfo_screenheight() - 30

    def support_variables():
        self.int_var_type_1 = IntVar()
        self.int_var_type_2 = IntVar()
        self.int_var_type_3 = IntVar()
        self.int_var_type_4 = IntVar()
        self.int_var_type_5 = IntVar()

        self.string_var_type = StringVar()

    #----------------------------------------------------------------------
    gui_mechanism_variables()
    support_variables()

'''------------------------------------------------------------------------------------------------------------------'''
def set_variable_default_values(self):
    def support_variables():
        self.int_var_type_1.set(True)
        self.int_var_type_2.set(False)
        self.int_var_type_3.set(True)
        self.int_var_type_4.set(False)
        self.int_var_type_5.set(True)

        self.string_var_type.set("default_value")

    #----------------------------------------------------------------------
    support_variables()
