from tkinter import LabelFrame

'''
https://www.tutorialspoint.com/python/tk_labelframe.htm
'''

def labelframe(label, column = 0, row = 0, text = "", columnspan = 1, rowspan = 1, sticky="nesw", bd = 5, width=0,
               background="#cfd1cf"):
    label = LabelFrame(label, text=text, background=background, bd=bd, width=width)
    label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return label
