class Paper:
    def __init__(self, strings):
        self.dots = {}
        for coord in strings:
            x = int(coord[0])
            y = int(coord[1])
            self.dots[f"x{x}y{y}"] = {"x" : x, "y" : y}

    def fold(self, axis, value):
        dots_to_remove = set()
        dots_to_add = {}
        for dot in self.dots:
            if self.dots[dot][axis] > value:
                dots_to_remove.add(dot)
                new_coord = value - (self.dots[dot][axis] - value)
                if axis == "x":
                    new_name = f"x{new_coord}y{self.dots[dot]['y']}"
                    dots_to_add[new_name] = {"x" : new_coord, "y" : self.dots[dot]["y"]}
                else:
                    new_name = f"x{self.dots[dot]['x']}y{new_coord}"
                    dots_to_add[new_name] = {"x" : self.dots[dot]["x"], "y" : new_coord}
        # print("Add ", dots_to_add)
        # print("Remove ", dots_to_remove)
        for dot in dots_to_remove:
            self.dots.pop(dot)
        self.dots.update(dots_to_add)
    
    def __str__(self):
        x_values = []
        y_values = []
        for dot in self.dots:
            x_values.append(self.dots[dot]["x"])
            y_values.append(self.dots[dot]["y"])
        max_x = max(x_values)
        max_y = max(y_values)
        display = []
        for y in range(max_y + 1):
            display.append([])
            for x in range(max_x + 1):
                display[y].append(".")
        for dot in self.dots:
            display[self.dots[dot]["y"]][self.dots[dot]["x"]] = "#"
        display_string = ""
        for line in display:
            line_string = "".join(line)
            display_string += line_string + "\n"
        return display_string

