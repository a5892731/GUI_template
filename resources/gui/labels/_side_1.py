from tkinter import *
from PIL import Image, ImageTk

from resources.gui.widgets.checkbox import checkbox
from resources.gui.widgets.button import button
from resources.gui.widgets.labelframe import labelframe
from resources.gui.widgets.entry import entry
from resources.gui.functions.import_image import import_image
from resources.gui.widgets.label_image import label_image

def side_1_label(self):

    def configure_central_label(window_width, window_height):
        '''configure main label'''
        self.main_label.columnconfigure(0, minsize=int(window_width))
        self.main_label.rowconfigure(0, minsize=int(window_height / 2))
        self.main_label.rowconfigure(1, minsize=int(window_height / 2))

    def configure_upper_label(window_width):
        upper_label = labelframe(label= self.main_label, column = 0, row = 0, text = "TEST LABEL")
        upper_label.columnconfigure(0, minsize=int(window_width / 2))
        upper_label.columnconfigure(1, minsize=int(window_width / 2))

        checkbox_label = labelframe(label= upper_label, column = 0, row = 0, text = "Checkboxes")

        checkbox(label=checkbox_label, name="int_var_type_1", variable=self.int_var_type_1, row=0)
        checkbox(label=checkbox_label, name="int_var_type_2", variable=self.int_var_type_2, row=1)
        checkbox(label=checkbox_label, name="int_var_type_3", variable=self.int_var_type_3, row=2)
        checkbox(label=checkbox_label, name="int_var_type_4", variable=self.int_var_type_4, row=3)
        checkbox(label=checkbox_label, name="int_var_type_5", variable=self.int_var_type_5, row=4)

    def configure_lower_label(window_width):
        lower_label = labelframe(label= self.main_label, column = 0, row = 1, text = "TEST LABEL 2")
        lower_label.columnconfigure(0, minsize=int(window_width / 2))
        lower_label.columnconfigure(1, minsize=int(window_width / 2))

        buttons_label = labelframe(label= lower_label, column = 0, row = 0, text = "Buttons")
        button(label=buttons_label, text="button_1", command=button_1_function, column=0, row=0)
        button(label=buttons_label, text="button_2", command=button_2_function, column=1, row=0)
        button(label=buttons_label, text="button_3", command=button_3_function, column=0, row=1)
        button(label=buttons_label, text="button_4", command=button_4_function, column=1, row=1)

        entry_label = labelframe(label= lower_label, column = 1, row = 0, text = "Entrtys")
        entry(label= entry_label, text=self.string_var_type, column=0, row=0, width=12)
        entry(label= entry_label, text=self.string_var_type, column=1, row=0, width=12)
        entry(label= entry_label, text=self.string_var_type, column=0, row=1, width=22)
        entry(label= entry_label, text=self.string_var_type, column=1, row=1, width=22)



        self.image = import_image(addres='resources/gui/pictures/iss_hd_dragon4.jpg', size=int(window_width / 2))
        label_image(label=lower_label, image=self.image, column = 0, row = 1,)





    '''----------------------------------------------BUTTONS----------------------------------------------------->>>>'''
    def button_1_function():
        print("button 1 click")
        self.int_var_type_1.set(False)

    def button_2_function():
        print("button 2 click")
        self.int_var_type_1.set(True)

    def button_3_function():
        print("button 3 click")
        self.int_var_type_2.set(False)

    def button_4_function():
        print("button 4 click")
        self.int_var_type_2.set(True)
    '''----------------------------------------------BUTTONS-----------------------------------------------------<<<<'''



    '''--------------------------------------------------------------------------------------------------------------'''
    window_width = 1048
    window_height = 554
    configure_central_label(window_width, window_height)
    configure_upper_label(window_width, )
    configure_lower_label(window_width, )




