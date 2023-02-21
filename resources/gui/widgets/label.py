from tkinter import Label, LEFT, CENTER

'''
https://www.tutorialspoint.com/python/tk_label.htm
'''

def label(label, column = 0, row = 0, text = "", columnspan = 1, rowspan=1, background="#cfd1cf", font=("Arial", 10),
          sticky="nesw", width = 0, justify=CENTER):
    label = Label(label, font=font, text=text, background=background, justify=justify, width=width)
    label.grid(column=column, row=row, columnspan=columnspan, rowspan=rowspan, sticky=sticky)
    return label

