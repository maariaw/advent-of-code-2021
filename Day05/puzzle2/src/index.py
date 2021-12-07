from inputreader import InputReader
from line import Line
from map import Map

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day05/input.txt"
    reader = InputReader(path)
    row_list = reader.get_list_of_lists()

    line_list = [Line(row[0], row[2]) for row in row_list]
    # for line in line_list:
    #     print(line)
    
    maximum_width = max(line_list, key=lambda line: line.get_max_width()).get_max_width()
    print("Max width: ", maximum_width)
    maximum_height = max(line_list, key=lambda line: line.get_max_height()).get_max_height()
    print("Max height: ", maximum_height)
    map = Map(maximum_width + 1, maximum_height + 1)

    for line in line_list:
        # print(line)
        map.add_line(line)

    # print(map)

    count = map.count_overlapping()

    print("Two or more lines overlap in ", count, " points")

if __name__ == "__main__":
    main()