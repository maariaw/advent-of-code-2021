class Map:
    def __init__(self, width, height):
        self.map = []
        for i in range(height):
            self.map.append([0] * width)

    def add_line(self, line):
        if line.is_horizontal():
            y = line.start[1]
            start = min(line.start[0], line.end[0])
            end = max(line.start[0], line.end[0]) + 1
            process = ""
            for x in range(start, end):
                self.map[y][x] += 1
                process += f"Mapped x:{x}, y:{y}\n"
            # print(process)
        elif line.is_vertical():
            x = line.start[0]
            start = min(line.start[1], line.end[1])
            end = max(line.start[1], line.end[1]) + 1
            process = ""
            for y in range(start, end):
                self.map[y][x] += 1
                process += f"Mapped x:{x}, y:{y}\n"
            # print(process)
        else:
            start_x = line.start[0]
            end_x = line.end[0]
            if end_x - start_x > 0:
                step_x = 1
            else:
                step_x = -1
            y = line.start[1]
            if line.end[1] - y > 0:
                step_y = 1
            else:
                step_y = -1
            process = ""
            for x in range(start_x, end_x + step_x, step_x):
                self.map[y][x] += 1
                process += f"Mapped x:{x}, y:{y}\n"
                y += step_y
            # print(process)
    
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
