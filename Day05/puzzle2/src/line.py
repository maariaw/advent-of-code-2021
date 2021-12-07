class Line:
    def __init__(self, start, end):
        first = start.split(",")
        second = end.split(",")
        self.start = [int(first[0]), int(first[1])]
        self.end = [int(second[0]), int(second[1])]
    
    def not_diagonal(self):
        return self.is_vertical() or self.is_horizontal()
    
    def is_vertical(self):
        return self.start[0] == self.end[0]
    
    def is_horizontal(self):
        return self.start[1] == self.end[1]
    
    def get_max_width(self):
        return max(self.start[0], self.end[0])
    
    def get_max_height(self):
        return max(self.start[1], self.end[1])
    
    def __str__(self):
        return f"{self.start} -> {self.end}"