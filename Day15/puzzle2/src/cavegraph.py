from heapq import heappush, heappop

class CaveGraph:
    def __init__(self, string_list):
        self.x_max = len(string_list[0])
        self.y_max = len(string_list)
        self.adjacency = self.get_adjacency(string_list)
        self.lowest_risk = 9999
        

    def get_adjacency(self, string_list):
        adjacency = {}
        grid_y_max = 5 * self.y_max
        grid_x_max = 5 * self.x_max
        for y in range(grid_y_max):
            for x in range(grid_x_max):
                node = (y, x)
                paths = {}
                for coord in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]:
                    new_y = coord[0]
                    new_x = coord[1]
                    value_modifier = 0
                    if new_y < 0 or new_x < 0 or new_y >= grid_y_max or new_x >= grid_x_max:
                        continue
                    if new_y >= self.y_max:
                        quotient = new_y // self.y_max
                        modulo = new_y % self.y_max
                        new_y = modulo
                        value_modifier += quotient
                    if new_x >= self.x_max:
                        quotient = new_x // self.x_max
                        modulo = new_x % self.x_max
                        new_x = modulo
                        value_modifier += quotient
                    value = int(string_list[new_y][new_x]) + value_modifier
                    if value > 9:
                        value = value - 9
                    paths[coord] = value
                adjacency[node] = {}
                adjacency[node]["paths"] = paths
                adjacency[node]["distance"] = 9999
                # print(f" {node} has paths {adjacency[node]} ")
        return adjacency

    def find_lowest_risk(self):
        searched = set()
        node_heap = []
        heappush(node_heap, [0, (0, 0)])
        self.adjacency[(0, 0)]["distance"] = 0
        while len(node_heap) != 0:
            node = heappop(node_heap)[1]
            if node in searched:
                continue
            searched.add(node)
            for neighbor in self.adjacency[node]["paths"]:
                weight = self.adjacency[node]["paths"][neighbor]
                current_distance = self.adjacency[neighbor]["distance"]
                new_distance = self.adjacency[node]["distance"] + weight
                if new_distance < current_distance:
                    self.adjacency[neighbor]["distance"] = new_distance
                    heappush(node_heap, [new_distance, neighbor])
        return self.adjacency[(self.y_max * 5 - 1, self.x_max * 5 - 1)]["distance"]
