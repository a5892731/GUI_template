from resources.gui.widgets.button import button
from resources.gui.widgets.labelframe import labelframe

def left_menu_bar(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    menu = labelframe(self.left_menu_label, text="MENU")
    menu.grid(column=1, row=0, sticky="nesw")

    button(label=menu, text="Side 1", command=self.view_side_1_label, column=0, row=0)



    for i in range(1,16):
        button(label=menu, text="", command="", column=0, row=i)  # row space
    button(label=menu, text="Exit", command=self.exit_program, column=0, row=i+1)
'''------------------------------------------------------------------------------------------------------------------'''

def view_side_1_label(self):
    self.center_frame.destroy()
    self.center_frame = labelframe(self.window)
    self.center_frame.grid(column=1, row=1, sticky="nesw")
    self.draw_home_window()
    print("home window")



def exit_program(self): #in future: move exit function from gui to state machine
    self.window.destroy()