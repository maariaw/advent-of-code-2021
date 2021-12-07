class Map:
    def __init__(self, width, height):
        self.map = []
        for i in range(height):
            self.map.append([0] * width)

    def add_line(self, line):
        if line.is_horizontal():
            y = line.start[1]
            start = line.start[0]
            end = line.end[0] + 1
            for x in range(start, end):
                self.map[y][x] += 1
        elif line.is_vertical():
            x = line.start[0]
            start = line.start[1]
            end = line.end[1] + 1
            for y in range(start, end):
                self.map[y][x] += 1
    
    def count_overlapping(self):
        count = 0
        for row in self.map:
            for place in row:
                if place > 1:
                    count += 1
        return count

    def __str__(self):
        map_image = ""
        for row in self.map:
            for place in row:
                if place == 0:
                    map_image += ". "
                else:
                    map_image += str(place) + " "
            map_image += "\n"
        return map_image
