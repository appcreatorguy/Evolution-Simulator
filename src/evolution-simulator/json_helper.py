import json

def pretty(data):
    return json.dumps(json.loads(data),indent=1)
def convert_to_json(data):
    return json.pretty(data)
def open(filename):
    f = open(filename,"r")
    content = f.read()
    f.close()
    return convert_to_json(content)
def save(content,filename):
    f = open(filename,"w")
    f.write(pretty(content)+"\n")
    f.close