class Graph:
    def __init__(self, edges):
        self.adjacency = {}
        for edge in edges:
            if not self.adjacency.get(edge[0]):
                self.adjacency[edge[0]] = set()
            self.adjacency.get(edge[0]).add(edge[1])
            if not self.adjacency.get(edge[1]):
                self.adjacency[edge[1]] = set()
            self.adjacency.get(edge[1]).add(edge[0])

    def start_search(self):
        searched = set()
        paths = []
        path = ""
        self.search("start", searched, path, paths)
        return paths

    def search(self, node, searched, path, paths):
        if node in searched:
            return
        if node == "end":
            path += node
            paths.append(path)
            return
        path += node + ","
        if node.islower():
            searched.add(node)
        for neighbor in self.adjacency[node]:
            self.search(neighbor, searched, path, paths)
        if node.islower():
            searched.remove(node)

    def __str__(self):
        adjacency_string = ""
        for node, neighbors in self.adjacency.items():
            adjacency_string += f"From {node} you can access {neighbors}\n"
        return adjacency_string