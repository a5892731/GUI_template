from tkinter import Scale, HORIZONTAL, ACTIVE


def slider(label, variable, min=0, max=100, tickinterval= 100, orient=HORIZONTAL, resolution = 1, command = "",
           column=0, row=0, state = ACTIVE):
    s = Scale(label, variable=variable, from_=min, to=max, tickinterval=tickinterval, resolution=resolution,
              orient=orient, command=command, state=state)
    s.grid(column=column, row=row, sticky="wens")
