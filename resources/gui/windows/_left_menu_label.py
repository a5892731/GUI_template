from resources.gui.widgets.button import button
from resources.gui.widgets.labelframe import labelframe

def _left_menu_bar(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    def view_home_label():
        self.main_label.destroy()
        self.main_label = labelframe(self.window)
        self.main_label.grid(column=1, row=0, sticky="nesw")
        self._home_label() #----------------------------------------------------- ADD WINDOW NAME HERE
        print("view_home_label")

    def view_settings_label():
        self.main_label.destroy()
        self.main_label = labelframe(self.window)
        self.main_label.grid(column=1, row=0, sticky="nesw")
        self._settings_label() #----------------------------------------------------- ADD WINDOW NAME HERE
        print("view_setings_label")

    '''--------------------------------------------------------------------------------------------------------------'''

    menu = labelframe(self.left_menu_label, text="MENU")
    menu.grid(column=1, row=0, sticky="nesw")

    menu_row_size = 16
    '''buttons variable is a list of buttons names in order'''
    buttons = ["HOME",
               "SETTINGS",
              ]
    '''button_functions variable is a list of buttons call functions in order'''
    button_functions = [view_home_label,
                        view_settings_label,
                       ]

    for row in range(len(buttons)):
        button(label=menu, text=buttons[row], command=button_functions[row], column=0, row=row)

    for i in range(row + 1, menu_row_size - 1):
        button(label=menu, text="", command="", column=0, row=i)  # row space
    button(label=menu, text="Exit", command=self.exit_program, column=0, row=menu_row_size)
'''------------------------------------------------------------------------------------------------------------------'''


def exit_program(self): #in future: move exit function from gui to state machine
    self.window.destroy()