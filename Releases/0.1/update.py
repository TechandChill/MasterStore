import json

import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

def check_version():
    if(config["version"] >= config["latest_version"]):
        pass
    else:
        pass