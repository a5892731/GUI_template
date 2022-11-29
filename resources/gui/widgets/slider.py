from tkinter import Scale, HORIZONTAL


def slider(label, variable, min=0, max=100, tickinterval= 100, orient=HORIZONTAL, resolution = 1, column=0, row=0):
    s = Scale(label, variable=variable, from_=min, to=max, tickinterval=tickinterval, resolution=resolution, orient=orient)
    s.grid(column=column, row=row, sticky="wens")
