from heapq import heappush, heappop

class CaveGraph:
    def __init__(self, string_list):
        self.x_max = len(string_list[0])
        self.y_max = len(string_list)
        self.adjacency = self.get_adjacency(string_list)
        self.lowest_risk = 9999
        

    def get_adjacency(self, string_list):
        adjacency = {}
        for y in range(self.y_max):
            for x in range(self.x_max):
                node = (y, x)
                paths = {}
                for coord in [(y-1, x), (y, x-1), (y, x+1), (y+1, x)]:
                    if coord[0] < 0 or coord[0] >= self.y_max:
                        continue
                    if coord[1] < 0 or coord[1] >= self.x_max:
                        continue
                    paths[coord] = int(string_list[coord[0]][coord[1]])
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
        return self.adjacency[(self.y_max - 1, self.x_max - 1)]["distance"]
