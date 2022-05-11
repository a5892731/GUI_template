from tkinter import Checkbutton, NORMAL

def checkbox(label, name, variable, row, column=0, state=NORMAL):
    c = Checkbutton(label, font=("Arial", 12), text=name,
                    variable=variable,
                    onvalue=True, offvalue=False, height=0,
                    width=0, background="#cfd1cf", state=state)
    c.grid(column=column, row=row, sticky="wns")