from utils.read_file import ReadFile

EXAMPLE_FILE = './day_2/example.txt'
INPUT_FILE = './day_2/input.txt'

class SolutionDay2():
    def __init__(self):
        pass

    def convert_to_list(self, line):
        return [int(i) for i in line.split(' ')]
    
    def get_orientation(self, val_1, val_2):
        if val_1 == val_2:
            return 0
        elif val_1 < val_2:
            return 1
        else:
            return -1
        
    def check_diff(self, val_1, val_2):
        diff = abs(val_1 - val_2)
        if diff <= 3 and diff > 0:
            return True
        return False

    def is_list_safe(self, input_list):
        orientations = []
        diffs = []
        for i in range(len(input_list) - 1):
            orientations.append(self.get_orientation(input_list[i], input_list[i+1]))
            diffs.append(self.check_diff(input_list[i], input_list[i+1]))
        if all(diffs) and not (1 in orientations and -1 in orientations):
            return True
        return False

    def read_file(self, file_path):
        return ReadFile(file_path).read_lines()
    
    def is_any_sublist_safe(self, input_list):
        for i in range(len(input_list)):
            temp_list = input_list.copy()
            temp_list.pop(i)
            if self.is_list_safe(temp_list):
                return True
        return False

    def calculate_part_1(self):
        return sum([self.is_list_safe(self.convert_to_list(row)) for row in self.read_file(INPUT_FILE)])
    
    def calculate_part_2(self):
        return sum([self.is_any_sublist_safe(self.convert_to_list(row)) for row in self.read_file(INPUT_FILE)])