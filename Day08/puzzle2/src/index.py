from inputreader import InputReader
from display import Display

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day08/input.txt"
    reader = InputReader(path)
    notes = reader.get_tube_split_lines()
    displays = [
        Display(line[0].split(), line[1].split())
        for line in notes
    ]
    display_sum = 0
    for display in displays:
        display_sum += display.get_decoded_output()

    print(f"Sum of the output values is ", display_sum)

if __name__ == "__main__":
    main()