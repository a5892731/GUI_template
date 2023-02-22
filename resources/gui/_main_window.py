from resources.gui.widgets.labelframe import labelframe

def build_main_window(self):
    def draw_window_attributes():
        '''gui attributes'''
        self.window.title("GUI_program_name")
        #self.window.attributes('-fullscreen', True)
        self.window.geometry("{}x{}".format(self.window_width, self.window_height))
        #icon = PhotoImage(file = "files/icon.png")
        #self.window.resizable(width=False, height=False)
        #self.window.iconphoto(True, icon) # icon in upper, left corner of program window
        self.window.config(background = "#cfd1cf") # "hex color picker" search in google

    def main_window_grid():
        '''In the main window, insert the table with windows'''
        def left_menu_cell():
            self.window.columnconfigure(0, minsize=100)
            self.window.rowconfigure(0, minsize=self.window_height)

            self.left_menu_label = labelframe(label=self.window, column=0, row=0)

        def main_cell():
            self.window.columnconfigure(1, minsize = self.window_width - 100)
            #self.window.rowconfigure(0, minsize=self.window_height)

            self.main_label = labelframe(label=self.window, column=1, row=0)

        '''----------------------------------------------------------------------------------------------------------'''
        left_menu_cell()
        main_cell()

    def draw_default_labels():
        '''draw default windows on program start'''
        self._left_menu_bar()
        self._home_label()
    '''--------------------------------------------------------------------------------------------------------------'''
    draw_window_attributes()
    main_window_grid() #  <=============================================================== create here your main window shape
    draw_default_labels()

def update_window(self):
    try:
        self.window.update_idletasks()
        self.window.update()
    except:
        print("Program closed")
        quit()




