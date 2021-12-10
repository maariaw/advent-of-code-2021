from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day10/input.txt"
    reader = InputReader(path)
    chunk_lines = reader.get_string_list()

    pairs = {("(", ")"), ("[", "]"), ("{", "}"), ("<", ">")}
    points = {
        ")" : 3,
        "]" : 57,
        "}" : 1197,
        ">" : 25137
    }
    openings = []
    corrupt = []
    for line in chunk_lines:
        for char in line:
            if char in "([{<":
                openings.append(char)
                continue
            elif not openings:
                corrupt.append(char)
                break
            pair_candidate = (openings.pop(), char)
            if pair_candidate not in pairs:
                corrupt.append(char)
                break

    score = 0
    for illegal in corrupt:
        score += points.get(illegal)

    print(f"The total syntax error score is {score}")

if __name__ == "__main__":
    main()