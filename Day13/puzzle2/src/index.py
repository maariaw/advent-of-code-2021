from inputreader import InputReader
from paper import Paper

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day13/input.txt"
    reader = InputReader(path)
    dots = set()
    lines = reader.get_split_lines_by_separator(",")
    coordinates_as_strings = list(filter(lambda line: len(line) == 2, lines))
    folding_instructions = list(filter(lambda line: len(line) == 1, lines))

    paper = Paper(coordinates_as_strings)
    # print(paper)

    for instruction in folding_instructions:
        parts = instruction[0].split("=")
        axis = parts[0][-1]
        value = int(parts[1])
        print(f"Cut at {axis}={value} ")
        paper.fold(axis, value)

    print(paper)

    print(f"{len(paper.dots)} dots are visible after first fold")

if __name__ == "__main__":
    main()
