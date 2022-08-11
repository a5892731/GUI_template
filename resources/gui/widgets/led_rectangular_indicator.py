from resources.gui.widgets.label import label

'''
change color by:

sensor1_led.update(color = "red")

'''


def led_indicator(window, name = "", row=0, column=0, width=4, color="pink", sticky="w"):
    sensor1_led = label(window, background=color, text=name, width=width, column=column , row=row, sticky="w")
    return sensor1_led