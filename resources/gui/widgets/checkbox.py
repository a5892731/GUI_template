from tkinter import Checkbutton, NORMAL

def checkbox(label, name, variable, row=0, command=None, column=0, font=("Arial", 12), state=NORMAL, sticky="wns"):
    c = Checkbutton(label, font=font, text=name,
                    variable=variable, command = command,
                    onvalue=True, offvalue=False, height=0,
                    width=0, background="#cfd1cf", state=state,
                    )
    c.grid(column=column, row=row, sticky=sticky)