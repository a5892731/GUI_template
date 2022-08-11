from resources.gui.widgets.label import label

def empty_row(label_, row=0, column=0, width=0, font=("Arial", 12, ), space="",):
    label(label=label_, font=font, background="#cfd1cf", text=space, width=width).grid(column=column, row=row, sticky="wesn")