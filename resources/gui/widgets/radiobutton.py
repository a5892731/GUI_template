
from tkinter import Radiobutton, NORMAL

'''
text is a list of buttons names

value is a lists of variable values

'''






def radiobutton(label, variable, row, command, text, value, column=0, state=NORMAL):
    #text and value are lists

    size = len(text)

    for row_ in range(size):
        r = Radiobutton(label, font=("Arial", 10), text=text[row_], command=command,
                         variable=variable, value=value[row_], background="#cfd1cf")
        r.grid(column=column, row=row+row_, sticky="w")



