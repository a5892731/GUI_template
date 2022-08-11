from resources.gui.widgets.button import button
from resources.gui.widgets.labelframe import labelframe

def _left_menu_bar(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    def view_side_1_label():
        self.main_label.destroy()
        self.main_label = labelframe(self.window)
        self.main_label.grid(column=1, row=0, sticky="nesw")
        self._side_1_label() #----------------------------------------------------- ADD WINDOW NAME HERE
        print("Side 1")

    def view_side_2_label():
        self.main_label.destroy()
        self.main_label = labelframe(self.window)
        self.main_label.grid(column=1, row=0, sticky="nesw")
        self._side_2_label() #----------------------------------------------------- ADD WINDOW NAME HERE
        print("Side 2")

    def view_side_3_label():
        self.main_label.destroy()
        self.main_label = labelframe(self.window)
        self.main_label.grid(column=1, row=0, sticky="nesw")
        self._side_1_label() #----------------------------------------------------- ADD WINDOW NAME HERE
        print("Side 3")

    def view_side_4_label():
        self.main_label.destroy()
        self.main_label = labelframe(self.window)
        self.main_label.grid(column=1, row=0, sticky="nesw")
        self._side_1_label() #----------------------------------------------------- ADD WINDOW NAME HERE
        print("Side 4")

    '''--------------------------------------------------------------------------------------------------------------'''



    menu = labelframe(self.left_menu_label, text="MENU")
    menu.grid(column=1, row=0, sticky="nesw")

    menu_row_size = 16
    '''buttons variable is a list of buttons names in order'''
    buttons = ["page1",
               "page2",
               "page3",
               "page4"]
    '''button_functions variable is a list of buttons call functions in order'''
    button_functions = [view_side_1_label,
                        view_side_2_label,
                        view_side_3_label,
                        view_side_4_label]

    for row in range(len(buttons)):
        button(label=menu, text=buttons[row], command=button_functions[row], column=0, row=row)

    for i in range(row + 1, menu_row_size - 1):
        button(label=menu, text="", command="", column=0, row=i)  # row space
    button(label=menu, text="Exit", command=self.exit_program, column=0, row=menu_row_size)
'''------------------------------------------------------------------------------------------------------------------'''



def exit_program(self): #in future: move exit function from gui to state machine
    self.window.destroy()