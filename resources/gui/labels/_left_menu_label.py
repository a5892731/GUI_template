from tkinter import *

from resources.gui.widgets.button import button

def left_menu_bar(self):
    '''--------------------------------------------------------------------------------------------------------------'''

    menu = LabelFrame(self.left_menu_label, text="MENU", background="#cfd1cf", bd=5)
    menu.grid(column=1, row=0, sticky="nesw")

    button(label=menu, text="", command="", column=0, row=0)  # row space

    button(label=menu, text="Side 1", command=self.view_side_1, column=0, row=1)
    button(label=menu, text="Side 2", command=self.view_side_2, column=0, row=2)

    button(label=menu, text="", command="", column=0, row=3)  # row space
    button(label=menu, text="", command="", column=0, row=4)  # row space
    button(label=menu, text="", command="", column=0, row=5)  # row space
    button(label=menu, text="", command="", column=0, row=6)  # row space
    button(label=menu, text="", command="", column=0, row=7)  # row space
    button(label=menu, text="", command="", column=0, row=8)  # row space

    button(label=menu, text="Exit", command=self.exit_program, column=0, row=9)
'''------------------------------------------------------------------------------------------------------------------'''
def view_side_1(self):
    self.main_label.destroy()
    self.main_label = LabelFrame(self.window, background="#cfd1cf", bd=5)
    self.main_label.grid(column=1, row=0, sticky="nesw")

    self.side_1_label() # resources/gui/labels/_side_1.py
    print("Side 1")

def view_side_2(self):
    self.main_label.destroy()
    self.main_label = LabelFrame(self.window, background="#cfd1cf", bd=5)
    self.main_label.grid(column=1, row=0, sticky="nesw")

    self.side_2_label()  # resources/gui/labels/_side_2.py
    print("Side 2")

def exit_program(self):
    self.window.destroy()