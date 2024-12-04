class ReadFile():
    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        with open(self.file_path, 'r') as f:
            return f.read()
        
    def read_lines(self):
        with open(self.file_path, 'r') as f:
            for line in f.readlines():
                yield line.replace("\n", "")