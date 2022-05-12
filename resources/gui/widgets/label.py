from tkinter import Label

'''
https://www.tutorialspoint.com/python/tk_label.htm
'''

def labelframe(label, column = 0, row = 0, text = "", columnspan = 1, background="#cfd1cf"):
    label = Label(label, font=("Arial", 12), text=text, background=background)
    label.grid(column=column, row=row, columnspan=columnspan, sticky="nesw")
    return label

