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

    first_instruction = folding_instructions[0][0].split("=")
    first_axis = first_instruction[0][-1]
    first_cutoff = int(first_instruction[1])
    print(f"Cut at {first_axis}={first_cutoff} ")

    paper.fold(first_axis, first_cutoff)
    # print(paper)

    print(f"{len(paper.dots)} dots are visible after first fold")

if __name__ == "__main__":
    main()
