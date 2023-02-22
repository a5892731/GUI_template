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

def _settings_label(self):
    '''--------------------------------------------------------------------------------BUTTONS----------------------'''

    '''-------------------------------------------------------------------------DRAWING FUNCTIONS--------------------'''


    '''------------------------------------------------------------------------------WINDOW FUNCTIONS----------------'''
    def window_settings():
        self.window_width = 1048
        self.window_hight = 554

        self.main_label.columnconfigure(0, minsize=int(self.window_width))
        self.main_label.rowconfigure(0, minsize=int(self.window_hight))


    '''--------------------------------------------------------------------------------------------------------------'''
    def window_upper_label(columns=4): #-----------------------------------------------------------------------------<<<<<<<<<<<

        '''---------------------------------------------------------------------------------------------------------'''
        upper_label = labelframe(self.main_label, text="COM Port settings", column=0, row=0, columnspan=1)

        '''
        baudrate: 9600
        port: COM3
        bytesize: 8
        parity: N
        stopbits: 1
        xonxoff: False
        rtscts: False
        write_timeout: None
        dsrdtr: False
        inter_byte_timeout: None
        timeout: 0.01
        exclusive: None
        '''

        label(label=upper_label, column=0, row=0, text="baudrate", rowspan=1)
        label(label=upper_label, column=0, row=1, text="port", rowspan=1)
        label(label=upper_label, column=0, row=2, text="bytesize", rowspan=1)
        label(label=upper_label, column=0, row=3, text="parity", rowspan=1)
        label(label=upper_label, column=0, row=4, text="xonxoff", rowspan=1)
        label(label=upper_label, column=0, row=5, text="rtscts", rowspan=1)
        label(label=upper_label, column=0, row=6, text="write_timeout", rowspan=1)
        label(label=upper_label, column=0, row=7, text="dsrdtr", rowspan=1)
        label(label=upper_label, column=0, row=8, text="inter_byte_timeout", rowspan=1)
        label(label=upper_label, column=0, row=9, text="timeout", rowspan=1)
        label(label=upper_label, column=0, row=10, text="exclusive", rowspan=1)


        entry(label=upper_label, text = "", column=1, row=0, width=16)
        entry(label=upper_label, text = "", column=1, row=1, width=16)
        entry(label=upper_label, text = "", column=1, row=2, width=16)
        entry(label=upper_label, text = "", column=1, row=3, width=16)
        entry(label=upper_label, text = "", column=1, row=4, width=16)
        entry(label=upper_label, text = "", column=1, row=5, width=16)
        entry(label=upper_label, text = "", column=1, row=6, width=16)
        entry(label=upper_label, text = "", column=1, row=7, width=16)
        entry(label=upper_label, text = "", column=1, row=8, width=16)
        entry(label=upper_label, text = "", column=1, row=9, width=16)
        entry(label=upper_label, text = "", column=1, row=10, width=16)

        empty_row(label_=upper_label, row=11)

        button(label=upper_label, text="Change Settings", command=change_settings, column=0, row=12, width=12,
               font=("Arial", 10, "bold"),columnspan=2)
    '''--------------------------------------------------------------------------------------------------------------'''
    def change_settings():
        print("change UDP settings")

    '''-----------------------------------------------------------------------------------MAIN-----------------------'''
    window_settings()
    '''--------------------------------------------------------------------------------------------------------------'''
    window_upper_label()
    '''--------------------------------------------------------------------------------------------------------------'''
