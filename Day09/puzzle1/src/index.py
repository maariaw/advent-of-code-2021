from inputreader import InputReader
from heightmap import HeightMap

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day09/input.txt"
    reader = InputReader(path)
    heights = reader.get_string_list()
    heightmap = HeightMap(heights)

    risk = heightmap.get_risk()

    print(f"The sum of the risk levels of all low points is {risk}")

if __name__ == "__main__":
    main()