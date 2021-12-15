from octopus import Octopus

class OctopusMapper:
    def __init__(self, string_list):
        self.map = {}

        for y in range(10):
            for x in range(10):
                location = (y, x)
                value = string_list[y][x]
                neighbors = set()
                for y_coord in range(y - 1, y + 2):
                    if y_coord < 0 or y_coord > 9:
                        continue
                    for x_coord in range(x - 1, x + 2):
                        if x_coord < 0 or x_coord > 9:
                            continue
                        if y_coord == y and x_coord == x:
                            continue
                        neighbors.add((y_coord, x_coord))
                self.map[location] = Octopus(location, value, neighbors)

    def do_step(self):
        for octopus in self.map.values():
            octopus.increase_value()
        return self.do_flashes()

    def do_flashes(self):
        flashed = set()
        while (True):
            flashed_before = len(flashed)
            for octopus_location in self.map.keys():
                self.depth_search(octopus_location, flashed)
            flashed_now = len(flashed)
            if flashed_before == flashed_now:
                break
        # print(f"There were {len(flashed)} flashes")
        for octopus_location in flashed:
            self.map.get(octopus_location).reset_value()
        return len(flashed)

    def depth_search(self, octopus_location, flashed):
        octopus = self.map.get(octopus_location)
        if octopus_location in flashed or not octopus.flash():
            return
        flashed.add(octopus_location)
        
        for neighbor in octopus.neighbors:
            self.map.get(neighbor).increase_value()
            self.depth_search(neighbor, flashed)
    
    def get_display(self):
        display = ""
        for y in range(10):
            for x in range(10):
                octopus = self.map.get((y, x))
                display += str(octopus.value)
            display += "\n"
        return display

    
    def __str__(self):
        map_string = ""
        for octopus in self.map.values():
            map_string += str(octopus) + "\n"
        return map_string
