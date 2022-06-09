class InputFile:
    def __init__(self, path: str):
        self.path = path
    
    def get_name(self):
        return self.path.split("/")[-1]