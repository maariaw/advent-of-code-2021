class HeightMap:
    def __init__(self, heights):
        self.mapping = [
            [int(digit) for digit in row]
            for row in heights
        ]
        self.x_bounds = len(heights[0])
        self.y_bounds = len(heights)
    
    def get_risk(self):
        return sum([height + 1 for height in self.find_low_points()])
    
    def find_low_points(self):
        lows = []
        for x in range(self.x_bounds):
            for y in range(self.y_bounds):
                if self.is_low_point(x, y):
                    lows.append(self.mapping[y][x])
        # print("The lows are: ", lows)
        return lows
    
    def is_low_point(self, x, y):
        for neighbor in self.get_neighbors(x, y):
            if neighbor <= self.mapping[y][x]:
                # print(f"{neighbor} is lower than {self.mapping[y][x]}")
                return False
        # print(self.mapping[y][x], " is a low point")
        return True

    def get_neighbors(self, x, y):
        steps = [-1, 1]
        neighbors = []
        for step in steps:
            if 0 <= x + step < self.x_bounds:
                neighbors.append(self.mapping[y][x + step])
            if 0 <= y + step < self.y_bounds:
                neighbors.append(self.mapping[y + step][x])
        # print("Neighbors are ", neighbors)
        return neighbors
