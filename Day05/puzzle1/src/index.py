from inputreader import InputReader
from line import Line
from map import Map

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day05/input.txt"
    reader = InputReader(path)
    row_list = reader.get_list_of_lists()

    line_list = [Line(row[0], row[2]) for row in row_list]
    non_diagonal = [line for line in line_list if line.not_diagonal()]
    # for line in non_diagonal:
    #     print(line)
    
    maximum_width = max(non_diagonal, key=lambda line: line.end[0]).end[0]
    # print("Max width: ", maximum_width)
    maximum_height = max(non_diagonal, key=lambda line: line.end[1]).end[1]
    # print("Max height: ", maximum_height)
    map = Map(maximum_width + 1, maximum_height + 1)

    for line in non_diagonal:
        map.add_line(line)

    # print(map)

    count = map.count_overlapping()

    print("Two or more lines overlap in ", count, " points")

if __name__ == "__main__":
    main()