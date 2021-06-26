import json


def pretty(data):
    return json.dumps(json.loads(data), indent=1)


def convert_to_json(data):
    data = json.dumps(data)
    return pretty(data)


def open_file(filename):
    f = open(filename, "r")
    content = f.read()
    f.close()
    return convert_to_json(content)


def save_to_file(content, filename):
    f = open(filename, "a")
    f.write("," + "\n" + pretty(content))
    f.close()