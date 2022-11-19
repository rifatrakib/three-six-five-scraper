import json


def read_secrets(name):
    with open(f"secrets/{name}.json") as reader:
        data = json.loads(reader.read())

    return data
