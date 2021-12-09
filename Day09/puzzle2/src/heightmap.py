class HeightMap:
    def __init__(self, heights):
        self.mapping = [
            [int(digit) for digit in row]
            for row in heights
        ]
        self.x_bounds = len(heights[0])
        self.y_bounds = len(heights)

    def get_product_of_three_largest_basins(self):
        basin_sizes = [
            self.get_basin_size(point)
            for point in self.find_low_points()
        ]
        biggest_three = []
        product = 1
        while len(biggest_three) < 3:
            next_biggest = max(basin_sizes)
            product = product * next_biggest
            biggest_three.append(next_biggest)
            basin_sizes.remove(next_biggest)
        return product
    
    def find_low_points(self):
        lows = set()
        for x in range(self.x_bounds):
            for y in range(self.y_bounds):
                if self.is_low_point(y, x):
                    lows.add((y, x))
        # print("The lows are: ", lows)
        return lows
    
    def is_low_point(self, y, x):
        for neighbor in self.get_neighbors(y, x):
            if self.mapping[neighbor[0]][neighbor[1]] <= self.mapping[y][x]:
                # print(f"{neighbor} is lower than {self.mapping[y][x]}")
                return False
        # print(self.mapping[y][x], " is a low point")
        return True
    
    def get_neighbors(self, y, x):
        steps = [-1, 1]
        neighbors = set()
        for step in steps:
            if 0 <= x + step < self.x_bounds:
                neighbors.add((y, x + step))
            if 0 <= y + step < self.y_bounds:
                neighbors.add((y + step, x))
        # print("Neighbors are ", neighbors)
        return neighbors
    
    def get_basin_size(self, low_point):
        basin = set()
        self.depth_search(basin, low_point)
        return len(basin)
    
    def depth_search(self, basin, point):
        if point in basin:
            return
        basin.add(point)
        for neighbor in self.get_neighbors(point[0], point[1]):
            if self.mapping[neighbor[0]][neighbor[1]] < 9:
                self.depth_search(basin, neighbor)

