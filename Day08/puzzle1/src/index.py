from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day08/input.txt"
    reader = InputReader(path)
    notes = reader.get_tube_split_lines()
    outputs = [
        parts[1].split()
        for parts in notes
    ]
    digit_sizes = []
    for digits in outputs:
        for digit in digits:
            digit_sizes.append(len(digit))

    count = 0
    for number in [2, 3, 4, 7]:
        count += digit_sizes.count(number)

    print(f"Digits 1, 4, 7 and 8 appear {count} times")

if __name__ == "__main__":
    main()