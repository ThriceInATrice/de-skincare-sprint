import json, re

def json_converter(path):
    with open(path, "r") as file:

        json_list = json.loads(file.read())

    path_data = re.split("[/.]", path)
    new_path = "/".join(path_data[:-1]) + ".jsonl"

    new_file = open(new_path, "w")

    for item in json_list:
        new_file.write(json.dumps(item) + "\n")
    

file_path = "data/makeup/products.json"
json_converter(file_path)