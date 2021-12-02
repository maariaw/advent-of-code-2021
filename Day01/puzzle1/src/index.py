from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day01/input.txt"
    reader = InputReader(path)
    depths = reader.get_int_list()

    increases = 0
    previous = depths[0]
    for depth in depths[1:]:
        if depth > previous:
            increases += 1
        previous = depth

    print("Number of depth measurement increases was ", increases)

if __name__ == "__main__":
    main()
