class Line:
    def __init__(self, start, end):
        first = start.split(",")
        second = end.split(",")
        first = [int(first[0]), int(first[1])]
        second = [int(second[0]), int(second[1])]
        self.start = [min(first[0], second[0]), min(first[1], second[1])]
        self.end = [max(first[0], second[0]), max(first[1], second[1])]
    
    def not_diagonal(self):
        return self.is_vertical() or self.is_horizontal()
    
    def is_vertical(self):
        return self.start[0] == self.end[0]
    
    def is_horizontal(self):
        return self.start[1] == self.end[1]
    
    def __str__(self):
        return f"{self.start} -> {self.end}"