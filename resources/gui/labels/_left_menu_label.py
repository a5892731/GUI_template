from tkinter import *

def left_menu_bar(self):

    def draw_button(label, name, function, row = 0):
        button = Button(label, font=("Arial", 12, "bold"), text=name, command=function)
        button.grid(column=0, row=row, sticky="we")
        return button
    '''--------------------------------------------------------------------------------------------------------------'''
    self.left_menu_label.columnconfigure(0, minsize=100)

    draw_button(label=self.left_menu_label, name="", function="", row=0)  # row space

    draw_button(label=self.left_menu_label, name="Side 1", function=self.view_side_1, row = 1)
    draw_button(label=self.left_menu_label, name="Side 2", function=self.view_side_2, row = 2)

    draw_button(label=self.left_menu_label, name="", function="", row=3)  # row space
    draw_button(label=self.left_menu_label, name="", function="", row=4)  # row space
    draw_button(label=self.left_menu_label, name="", function="", row=5)  # row space
    draw_button(label=self.left_menu_label, name="", function="", row=6)  # row space
    draw_button(label=self.left_menu_label, name="", function="", row=7)  # row space
    draw_button(label=self.left_menu_label, name="", function="", row=8)  # row space

    draw_button(label=self.left_menu_label, name="Exit", function=self.exit_program, row = 9)
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