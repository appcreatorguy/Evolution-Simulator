import json
import os
from colorama import Fore


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


def save(content, filename):
    os.makedirs(
        os.path.dirname(filename), exist_ok=True
    )  # Create intermediate directories if necessary.
    f = open(filename, "a")
    f.write(convert_to_json(content) + "\n")
    f.close


def array_write(filename, data):
    """Writes to a JSON file that contains multiple objects, in a nested array.

    Args:
        filename: The name of the file to write to.
        data: The data to write to the file.
    """
    os.makedirs(
        os.path.dirname(filename), exist_ok=True
    )  # Create intermediate directories if necessary.
    if not os.path.isfile(filename):  # Create empty JSON array if file doesn't exist.
        f = open(filename, "x")
        f.write("[]")
        f.close()
    print(Fore.MAGENTA + "Writing Data to File...")
    if os.path.getsize(filename) == 2:  # If this is the first object in the array
        data_to_write = convert_to_json(data) + "]"
    else:
        data_to_write = "," + convert_to_json(data) + "]"
    f = open(filename, "a")
    f.seek(0)
    f.seek(os.path.getsize(filename) - 1)
    f.truncate()
    f.write(data_to_write)
    f.close()
