from tkinter import *

from resources.gui.widgets.button import button

def left_menu_bar(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    menu = LabelFrame(self.left_menu_label, text="MENU", background="#cfd1cf", bd=5)
    menu.grid(column=1, row=0, sticky="nesw")

    button(label=menu, text="Side 1", command=self.view_side_1_label, column=0, row=0)

    for i in range(1,16):
        button(label=menu, text="", command="", column=0, row=i)  # row space
    button(label=menu, text="Exit", command=self.exit_program, column=0, row=i+1)
'''------------------------------------------------------------------------------------------------------------------'''

def view_side_1_label(self):
    self.tab_name = "view_side_1_label"
    self.main_label.destroy()
    self.main_label = LabelFrame(self.window, background="#cfd1cf", bd=5)
    self.main_label.grid(column=1, row=0, sticky="nesw")

    self.side_1_label() # resources/gui/labels/_side_1_label.py
    print("view_side_1_label")



def exit_program(self): #in future: move exit function from gui to state machine
    self.tab_name = "Exit"
    self.window.destroy()