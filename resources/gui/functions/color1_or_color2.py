def color1_or_color2(status, color1 = "green", color2 = "red"):
    if status:
        return color1
    else:
        return color2