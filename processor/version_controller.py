import json

class VersionController():
    def __init__(self, path: str):
        self.path = path
    
    def get(self):
        with open(self.path) as fp:
            return json.load(fp)