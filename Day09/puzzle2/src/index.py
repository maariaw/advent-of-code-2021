from inputreader import InputReader
from heightmap import HeightMap

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day09/input.txt"
    reader = InputReader(path)
    heights = reader.get_string_list()
    heightmap = HeightMap(heights)

    product = heightmap.get_product_of_three_largest_basins()

    print(f"The sizes of the three largest basins multiplied makes {product} ")

if __name__ == "__main__":
    main()