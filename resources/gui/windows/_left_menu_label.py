from resources.gui.widgets.button import button
from resources.gui.widgets.labelframe import labelframe
from resources.gui.widgets.entry import entry
from resources.gui.widgets.label import label


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



    program_performance = labelframe(self.left_menu_label, text="Program performance")
    program_performance.grid(column=1, row=1, sticky="nesw")

    label(label=program_performance, column=0, row=0, text="Thread1 timing:", rowspan=1, sticky="w")
    entry(label=program_performance, text=self.threat1_ms, column=0, row=1, width=16)

    label(label=program_performance, column=0, row=2, text="Thread2 timing:", rowspan=1, sticky="w")
    entry(label=program_performance, text=self.threat2_ms, column=0, row=3, width=16)

    label(label=program_performance, column=0, row=4, text="Thread3 timing:", rowspan=1, sticky="w")
    entry(label=program_performance, text=self.threat3_ms, column=0, row=5, width=16)
'''------------------------------------------------------------------------------------------------------------------'''


def exit_program(self): #in future: move exit function from gui to state machine
    self.window.destroy()