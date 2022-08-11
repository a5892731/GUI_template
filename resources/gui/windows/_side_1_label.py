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


def _side_1_label(self):
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

        def draw_tex_bar(window, row, column, width, height):
            drow_tex_bar_label = labelframe(window, column = column, row = row, text = "", columnspan = 1, rowspan = 1,
                                            sticky="nesw", bd = 5, width=0)
            text_box(drow_tex_bar_label, width=width, height=height, column=0, row=0, columnspan=1, sticky="w")

        '''---------------------------------------------------------------------------------------------------------'''
        upper_label = labelframe(self.main_label, text="...", column=0, row=0, columnspan=1)
        for row in range(columns):
            upper_label.columnconfigure(row, minsize=self.window_width/columns)

        draw_tex_bar(upper_label, row=0, column=0, width=37, height=10)
        draw_tex_bar(upper_label, row=0, column=1, width=37, height=10)
        draw_tex_bar(upper_label, row=0, column=2, width=37, height=10)

    def window_bottom_label(columns=4): #-----------------------------------------------------------------------------<<<<<<<<<<<

        '''---------------------------------------------------------------------------------------------------------'''
        bottom_label = labelframe(self.main_label, text="....", column=0, row=1, columnspan=1)
        for row in range(columns):
            bottom_label.columnconfigure(row, minsize=self.window_width/columns)


    '''-----------------------------------------------------------------------------------MAIN-----------------------'''
    window_settings()
    '''--------------------------------------------------------------------------------------------------------------'''
    window_upper_label()
    '''--------------------------------------------------------------------------------------------------------------'''
    window_bottom_label()