
def read_text_from_file(file_address, file_name):
    with open(file_address + "/" + file_name, encoding="UTF-8") as f:
        lines = f.readlines()

        text = ""
        for line in lines:
            text = text + line

        return text