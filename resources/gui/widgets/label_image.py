from tkinter import Label

'''
https://www.tutorialspoint.com/python/tk_label.htm
'''

def label_image(label, image, column = 0, row = 0, text = "", columnspan = 1, ):
    label = Label(label, font=("Arial", 12), image=image, text=text, background="#cfd1cf")
    label.grid(column=column, row=row, columnspan=columnspan, sticky="nesw")
    return label

