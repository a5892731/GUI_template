from tkinter import Entry

'''
https://www.tutorialspoint.com/python/tk_entry.htm
'''

def entry(label, text, column = 0, row = 0, width= 12, columnspan = 1):
    entry = Entry(label, font=("Arial", 15), textvariable=text, width=width)
    entry.grid(column=column, row=row, columnspan=columnspan, sticky="w")
    return entry

