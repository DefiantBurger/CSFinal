import json

class VersionController:
    def __init__(self, path: str):
        self.path = path
    
    def get(self) -> dict: 
        with open(self.path, 'r') as fp:
            return json.load(fp)
    
    def update(self, new):
        with open(self.path, 'w') as fp:
            return json.dump(new, fp, indent=2)