
from tkinter import Radiobutton, NORMAL

'''
text is a list of buttons names

value is a lists of variable values

'''



def radiobuttons(label, variable, row, command, text, value, column=0, state=NORMAL, select=0, style="wertical"):
    #text and value are lists
    #select is a number of radiobutton to be selected

    size = len(text)

    if style == "wertical":
        for row_ in range(size):
            r=Radiobutton(label, font=("Arial", 10), text=text[row_], command=command,
                             variable=variable, value=value[row_], background="#cfd1cf")
            r.grid(column=column, row=row+row_, sticky="w")


            if row_ == select:
                r.select()
            else:
                r.deselect()
    elif style == "horizontal":
        for column_ in range(size):
            r = Radiobutton(label, font=("Arial", 10), text=text[column_], command=command,
                            variable=variable, value=value[column_], background="#cfd1cf")
            r.grid(column=column+column_, row=row, sticky="w")

            if column_ == select:
                r.select()
            else:
                r.deselect()



def radiobutton(label, name, variable, row, column=0, command = "", value = True, select = False):
    c = Radiobutton (label, font=("Arial", 12), text=name,
                    variable=variable, value=value,
                    height=0,
                    width=0, background="#cfd1cf",
                    )
    c.grid(column=column, row=row, sticky="wns")

    if select:
        c.select()
    else:
        c.deselect()