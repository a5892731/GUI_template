from tkinter import Entry, LEFT

'''
https://www.tutorialspoint.com/python/tk_entry.htm
'''

def entry(label, text, column = 0, row = 0, width= 12, columnspan = 1, sticky="w", font=("Arial", 10), justify=LEFT):
    entry = Entry(label, font=font, textvariable=text, width=width, justify=justify)
    entry.grid(column=column, row=row, columnspan=columnspan, sticky=sticky)
    return entry

