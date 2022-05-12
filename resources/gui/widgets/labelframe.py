from tkinter import LabelFrame

'''
https://www.tutorialspoint.com/python/tk_labelframe.htm
'''

def labelframe(label, column = 0, row = 0, text = "", columnspan = 1):
    label = LabelFrame(label, text=text, background="#cfd1cf", bd=5)
    label.grid(column=column, row=row, columnspan=columnspan, sticky="nesw")
    return label
