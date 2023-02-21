from tkinter import Text, Scrollbar
from resources.gui.widgets.label import label

'''
https://www.obliczeniowo.com.pl/496

insert text by 
textbox.insert(tk.END, "{}\n".format(string)) # add line
textbox.see(END)  # move to end where textbox is return variable name


or 


textbox.insert("1.0", "{}".format(string))  # replace text


to delete text:
self.stage_description_text_box.delete('1.0', END)

'''

def text_box(window, width = 50, height = 10, column = 0, row = 0, columnspan = 1, sticky = "w", font=("Arial", 10)):

    textbox_label = label(label=window, row=row, column=column, columnspan = columnspan, font=font, sticky = "w")

    sb_textbox = Scrollbar(textbox_label, width = 20)  # tworzenie kontrolki paska przewijania
    textbox = Text(textbox_label, width = width, height = height, yscrollcommand = sb_textbox.set)
    textbox.grid(column=0, row=0, columnspan=columnspan, sticky=sticky)
    #sb_textbox.place(in_=textbox, relx=1., rely=0, relheight=1.)
    sb_textbox.grid(column=1, row=0, sticky="wns")

    sb_textbox.config(command=textbox.yview)

    return textbox

