

def side_2_label(self):

    def configure_central_label(window_width, window_height):
        '''configure main label'''

        self.main_label.columnconfigure(0, minsize=int(window_width))
        self.main_label.rowconfigure(0, minsize=int(window_height / 2))
        self.main_label.rowconfigure(1, minsize=int(window_height / 2))






    '''--------------------------------------------------------------------------------------------------------------'''
    window_width = 1048
    window_height = 554
    configure_central_label(window_width, window_height)





