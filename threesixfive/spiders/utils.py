import json


def read_secrets(name):
    with open(f"secrets/{name}.json") as reader:
        data = json.loads(reader.read())

    return data


def format_folder_and_file_name(name):
    mapper = {
        "\\": " ",
        "/": " ",
        ":": " - ",
        "*": " ",
        "?": "",
        '"': " - ",
        "<": " - ",
        ">": " - ",
        "|": " ",
    }
    formatted_chars = []
    for char in name:
        if char in mapper:
            formatted_chars.append(char.replace(char, mapper[char]))
        else:
            formatted_chars.append(char)

    formatted_name = "".join(formatted_chars)
    return formatted_name
