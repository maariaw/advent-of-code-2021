from graph import Graph
from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day12/input.txt"
    reader = InputReader(path)
    connections = reader.get_split_lines_by_separator("-")
    graph = Graph(connections)
    paths = graph.start_search()
    # print(graph)
    # for path in paths:
    #     print(path)

    print(f"There are {len(paths)} paths that visit small caves at most once")

if __name__ == "__main__":
    main()