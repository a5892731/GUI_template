from resources.gui.widgets.button import button
from resources.gui.widgets.labelframe import labelframe

def _left_menu_bar(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    menu = labelframe(self.left_menu_label, text="MENU")
    menu.grid(column=1, row=0, sticky="nesw")

    menu_row_size = 16
    buttons = ["page1",
               "page2",
               "page3",
               "page4"]
    button_functions = [self.view_side_1_label,
                        self.view_side_1_label,
                        self.view_side_1_label,
                        self.view_side_1_label]

    for row in range(len(buttons)):
        button(label=menu, text=buttons[row], command=button_functions[row], column=0, row=row)

    for i in range(row + 1, menu_row_size - 1):
        button(label=menu, text="", command="", column=0, row=i)  # row space
    button(label=menu, text="Exit", command=self.exit_program, column=0, row=menu_row_size)
'''------------------------------------------------------------------------------------------------------------------'''

def view_side_1_label(self):
    self.center_frame.destroy()
    self.center_frame = labelframe(self.window)
    self.center_frame.grid(column=1, row=1, sticky="nesw")
    self.draw_home_window()
    print("home window")



def exit_program(self): #in future: move exit function from gui to state machine
    self.window.destroy()