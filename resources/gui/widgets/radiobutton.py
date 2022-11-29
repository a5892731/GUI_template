
from tkinter import Radiobutton, NORMAL

'''
text is a list of buttons names

value is a lists of variable values

'''



def radiobuttons(label, variable, row, command, text, value, column=0, state=NORMAL):
    #text and value are lists

    size = len(text)

    for row_ in range(size):
        r = Radiobutton(label, font=("Arial", 10), text=text[row_], command=command,
                         variable=variable, value=value[row_], background="#cfd1cf")
        r.grid(column=column, row=row+row_, sticky="w")


def radiobutton(label, name, variable, row, column=0, command = "", value = True):
    c = Radiobutton (label, font=("Arial", 12), text=name,
                    variable=variable, value=value,
                    height=0,
                    width=0, background="#cfd1cf",
                    )
    c.grid(column=column, row=row, sticky="wns")
