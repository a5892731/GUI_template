from PIL import Image, ImageTk

def import_image(addres='resources/gui/pictures/iss_hd_dragon4.jpg', size=600):
    def re_sizer(image, max=size):
        width, height = image.size

        if height > width:
            scale = height / max
            width = width / scale
            height = height / scale
        else:
            scale = width / max
            width = width / scale
            height = height / scale
        return int(width), int(height)

    my_img = Image.open(addres)
    width, height = re_sizer(my_img)

    my_img = my_img.resize((width, height), Image.ANTIALIAS)
    image = ImageTk.PhotoImage(my_img)
    return image