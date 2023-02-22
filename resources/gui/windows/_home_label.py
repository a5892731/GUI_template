'''
-import this _function_label in ProgramRun class in main.pyw start file
-add reference to this function in chosen button in _left_menu_bar.py


'''

from resources.gui.widgets.labelframe import labelframe
from resources.gui.widgets.label import label
from resources.gui.widgets.entry import entry
from resources.gui.widgets.button import button
from resources.gui.widgets.checkbox import checkbox
from resources.gui.widgets.radiobutton import radiobutton
from resources.gui.widgets.text import text_box
from resources.gui.widgets.empty_row import empty_row
from resources.gui.widgets.led_rectangular_indicator import led_indicator
from resources.gui.widgets.text import text_box
from resources.gui.widgets.slider import slider


def _home_label(self):
    '''--------------------------------------------------------------------------------BUTTONS----------------------'''

    '''-------------------------------------------------------------------------DRAWING FUNCTIONS--------------------'''


    '''------------------------------------------------------------------------------WINDOW FUNCTIONS----------------'''
    def window_settings():
        self.window_width = 1048
        self.window_hight = 554

        self.main_label.columnconfigure(0, minsize=int(self.window_width))
        self.main_label.rowconfigure(0, minsize=int(self.window_hight / 2))
        self.main_label.rowconfigure(1, minsize=int(self.window_hight / 2))

    '''--------------------------------------------------------------------------------------------------------------'''
    def window_upper_label(columns=3): #-----------------------------------------------------------------------------<<<<<<<<<<<

        '''---------------------------------------------------------------------------------------------------------'''
        upper_label = labelframe(self.main_label, text="Read UDP", column=0, row=0, columnspan=1)

        _label = label(upper_label, column=0, row=0, columnspan=1)

        label(label=_label, column=0, row=0, text="ID [4 bytes]", rowspan=1)
        entry(label=_label, text = "", column=0, row=1, width=16)

        label(label=_label, column=1, row=0, text="DLC [1 byte]", rowspan=1)
        entry(label=_label, text = "", column=1, row=1, width=16)

        label(label=_label, column=2, row=0, text="reserved [3 bytes]", rowspan=1)
        entry(label=_label, text="", column=2, row=1, width=16)

        label(label=_label, column=3, row=0, text="data", rowspan=1)
        entry(label=_label, text="", column=3, row=1, width=96)

        empty_row(label_=upper_label, row=1)

        self.read_texbox = text_box(window=upper_label, width=125, height=10, column=0, row=2)


    def window_bottom_label(columns=4): #-----------------------------------------------------------------------------<<<<<<<<<<<

        '''---------------------------------------------------------------------------------------------------------'''
        bottom_label = labelframe(self.main_label, text="Send UDP", column=0, row=1, columnspan=1)

        _label = label(bottom_label, column=0, row=0, columnspan=1)

        label(label=_label, column=0, row=0, text="ID [4 bytes]", rowspan=1)
        entry(label=_label, text = "", column=0, row=1, width=16)

        label(label=_label, column=1, row=0, text="DLC [1 byte]", rowspan=1)
        entry(label=_label, text = "", column=1, row=1, width=16)

        label(label=_label, column=2, row=0, text="reserved [3 bytes]", rowspan=1)
        entry(label=_label, text="", column=2, row=1, width=16)

        label(label=_label, column=3, row=0, text="data", rowspan=1)
        entry(label=_label, text="", column=3, row=1, width=96)


        empty_row(label_=bottom_label, row=1)

        button(label=bottom_label, text="SEND", command=send_data, column=0, row=2, width=12,
               font=("Arial", 10, "bold"))

    '''--------------------------------------------------------------------------------------------------------------'''
    def send_data():
        print("send data button activated")


    '''-----------------------------------------------------------------------------------MAIN-----------------------'''
    window_settings()
    '''--------------------------------------------------------------------------------------------------------------'''
    window_upper_label()
    '''--------------------------------------------------------------------------------------------------------------'''
    window_bottom_label()