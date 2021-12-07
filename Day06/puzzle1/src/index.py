from inputreader import InputReader
from fish_tracker import FishTracker

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day06/input.txt"
    reader = InputReader(path)
    fish_ages = reader.get_one_line_ints()
    tracker = FishTracker(fish_ages)
    # print(tracker)
    days = 80
    for i in range(days):
        tracker.pass_day()
        # print(tracker)

    print(f"After {days} days here will be {len(tracker.fishies)} lanternfish")

if __name__ == "__main__":
    main()