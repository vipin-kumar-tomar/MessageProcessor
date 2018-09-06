import json
import os
import errno


def read_json_data_file(type,value):
    cwd = os.getcwd()
    pcwd = "\\".join(cwd.split('\\')[:-1])
    confdir = cwd + "\\config"
    try:
        dirExists = os.path.exists(confdir)
        if not dirExists:
            confdir = pcwd + "\\config"
    except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

    json_data = open(confdir+"\\config.json")
    data = json.load(json_data)
    try:
      return data[type][value]
    except:
      return None
