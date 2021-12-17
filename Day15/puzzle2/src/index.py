from inputreader import InputReader
from cavegraph import CaveGraph

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day15/input.txt"
    reader = InputReader(path)
    string_list = reader.get_string_list()
    graph = CaveGraph(string_list)
    lowest_risk = graph.find_lowest_risk()
    
    print(f"""
    The lowest total risk is {lowest_risk}
    """)

if __name__ == "__main__":
    main()
