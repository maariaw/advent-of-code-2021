from inputreader import InputReader

def main():
    days = 256
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day06/input.txt"
    reader = InputReader(path)
    fishes = reader.get_one_line_ints()

    fish_counts = {}

    for fish in fishes:
        fish_counts[fish] = fish_counts[fish] + 1 if fish in fish_counts else 1

    for day in range(days):
        new_fish_counts = {}
        for age in fish_counts:
            timer = age - 1
            if timer == -1:
                if 8 in new_fish_counts:
                    new_fish_counts[8] = new_fish_counts[8] + fish_counts[age]
                else:
                    new_fish_counts[8] = fish_counts[age]
                if 6 in new_fish_counts:
                    new_fish_counts[6] = new_fish_counts[6] + fish_counts[age]
                else:
                    new_fish_counts[6] = fish_counts[age]
            else:
                if timer in new_fish_counts:
                    new_fish_counts[timer] = new_fish_counts[timer] + fish_counts[age]
                else:
                    new_fish_counts[timer] = fish_counts[age]

        fish_counts = new_fish_counts

    print(f"After {days} days here will be {sum(fish_counts.values())} lanternfish")

if __name__ == "__main__":
    main()