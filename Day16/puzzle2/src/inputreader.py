class InputReader:
    def __init__(self, path):
        self.path = path
    
    def get_int_list(self):
        with open(self.path) as input:
            int_list = [
                int(line.strip())
                for line in input.readlines()
                if len(line) > 0
            ]

        return int_list

    def get_list_of_lists(self):
        with open(self.path) as input:
            list_list = [
                line.split()
                for line in input.readlines()
                if len(line) > 0
            ]

        return list_list
    
    def get_string_list(self):
        with open(self.path) as input:
            string_list = [
                line.strip()
                for line in input.readlines()
                if len(line) > 0
            ]

        return string_list
    
    def get_one_line_ints(self):
        with open(self.path) as input:
            int_list = [
                int(number)
                for number in input.readline().split(",")
            ]

        return int_list
    
    def get_one_line_string(self):
        with open(self.path) as input:
            string = input.readline().strip()
        return string

    def get_split_lines_by_separator(self, separator):
        with open(self.path) as input:
            split_lines = [
                line.strip().split(separator)
                for line in input.readlines()
                if len(line.strip()) > 0
            ]
        return split_lines
