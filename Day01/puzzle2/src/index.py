from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day01/input.txt"
    reader = InputReader(path)
    depths = reader.get_int_list()

    increases = 0
    previous = sum(depths[:3])
    for i in range(4, len(depths) + 1):
        print("Previous: ", previous)
        print(depths[i-3:i], "sum: ", sum(depths[i-3:i]))
        depth_sum = sum(depths[i-3:i])
        if depth_sum > previous:
            print("increased")
            increases += 1
        previous = depth_sum

    print("Number of depth measurement increases was ", increases)

if __name__ == "__main__":
    main()
