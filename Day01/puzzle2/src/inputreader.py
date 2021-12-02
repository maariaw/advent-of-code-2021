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
