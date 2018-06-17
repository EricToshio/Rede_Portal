import json

def redecasd_status():
    with open('redecasd_info.json') as f:
        data = json.load(f)
    return data