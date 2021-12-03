from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day02/input.txt"
    reader = InputReader(path)
    steps = reader.get_list_of_lists()

    # steps = [
    #     ["forward", "5"],
    #     ["down", "5"],
    #     ["forward", "8"],
    #     ["up", "3"],
    #     ["down", "8"],
    #     ["forward", "2"]
    # ]
    
    aim = 0
    total_down = 0
    total_horizontal = 0

    for step in steps:
        number = int(step[1])
        if step[0] == "forward":
            total_horizontal += number
            total_down += aim * number
        elif step[0] == "down":
            aim += number
        elif step[0] == "up":
            aim -= number
    

    print(
        "Final position was ",
        total_down,
        " depth and ",
        total_horizontal,
        " horizontal"
    )
    print("Horizontal by depth is ", total_down * total_horizontal)

if __name__ == "__main__":
    main()
