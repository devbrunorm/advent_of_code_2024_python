from utils.read_file import ReadFile

EXAMPLE_FILE = './day_1/example.txt'
INPUT_FILE = './day_1/input.txt'

class SolutionDay1():
    def __init__(self):
        self.reset_numbers()

    def reset_numbers(self):
        self.left_list = []
        self.right_list = []
        self.right_list_counter = {}

    def add_numbers_to_lists(self):
        self.reset_numbers()
        for line in ReadFile(INPUT_FILE).read_lines():
            numbers = line.split('   ')
            self.left_list.append(int(numbers[0]))
            self.right_list.append(int(numbers[1]))

    def calculate_part_1(self):
        self.add_numbers_to_lists()
        self.left_list.sort()
        self.right_list.sort()
        return sum([abs(i[0] - i[1]) for i in zip(self.left_list, self.right_list)])
    
    def create_right_list_counter(self):
        self.reset_numbers()
        for line in ReadFile(INPUT_FILE).read_lines():
            numbers = line.split('   ')
            left_number = int(numbers[0])
            right_number = int(numbers[1])
            self.left_list.append(left_number)
            if self.right_list_counter.get(right_number) is None:
                self.right_list_counter[right_number] = 1
            else:
                self.right_list_counter[right_number] += 1

    def multiply_count_dict(self, number):
        return self.right_list_counter.get(number, 0) * number
    
    def calculate_part_2(self):
        self.create_right_list_counter()
        return sum([self.multiply_count_dict(i) for i in self.left_list])