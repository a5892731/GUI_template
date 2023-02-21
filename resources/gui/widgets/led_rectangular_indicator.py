from resources.gui.widgets.label import label

'''
change color by:

sensor1_led.config(background = "red")

'''


def led_indicator(window, name = "", row=0, column=0, width=4, color="pink", sticky="w", rowspan=1):
    sensor1_led = label(window, background=color, text=name, width=width, column=column , row=row, sticky=sticky,
                        rowspan=rowspan)
    return sensor1_led