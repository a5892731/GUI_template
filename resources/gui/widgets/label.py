from tkinter import Label, LEFT, CENTER

'''
https://www.tutorialspoint.com/python/tk_label.htm
'''

def label(label, column = 0, row = 0, text = "", columnspan = 1, background="#cfd1cf", font=("Arial", 15),
          sticky="nesw", justify=CENTER):
    label = Label(label, font=font, text=text, background=background, justify=justify)
    label.grid(column=column, row=row, columnspan=columnspan, sticky=sticky)
    return label

