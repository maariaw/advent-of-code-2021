from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day10/input.txt"
    reader = InputReader(path)
    chunk_lines = reader.get_string_list()

    pairs = {
        "(" : ")",
        "[" : "]",
        "{" : "}",
        "<" : ">"
    }
    points = {
        ")" : 1,
        "]" : 2,
        "}" : 3,
        ">" : 4
    }
    
    closer_lines = []
    for line in chunk_lines:
        openings = []
        closers = []
        corrupt = False
        for char in line:
            if char in "([{<":
                openings.append(char)
                continue
            elif not openings:
                break
            if pairs.get(openings.pop()) != char:
                corrupt = True
                break
        if corrupt:
            continue
        for i in range(len(openings)):
            closers.append(pairs.get(openings.pop()))
        closer_lines.append(closers)
    
    line_scores = []
    for line in closer_lines:
        score = 0
        for closer in line:
            score = score * 5
            score += points.get(closer)
        line_scores.append(score)

    sorted_scores = sorted(line_scores)
    middle_score = sorted_scores[int(len(sorted_scores) / 2)]

    print(f"The autocomplete score is {middle_score}")

if __name__ == "__main__":
    main()