from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day14/input.txt"
    reader = InputReader(path)
    data = reader.get_split_lines_by_separator(" -> ")
    template = data[0][0]
    pairs = [(pair[0], pair[1]) for pair in data if len(pair) > 1]
    rules = {}
    for pair in list(filter(lambda line: len(line) > 1, pairs)):
        rules[pair[0]] = (f"{pair[0][0]}{pair[1]}", f"{pair[1]}{pair[0][1]}")
    # for rule in rules:
    #     print(rules[rule])

    polymer = {}

    for i in range(len(template) - 1):
        pair = template[i] + template[i + 1]
        if not polymer.get(pair):
            polymer[pair] = 1
        else:
            polymer[pair] += 1


    steps = 40
    counts = {}
    for char in template:
        if not counts.get(char):
            counts[char] = 1
        else:
            counts[char] += 1
    # print(counts)

    for step in range(steps):
        new_polymer = {}
        for pair in polymer:
            if pair in rules:
                amount = polymer[pair]
                char = rules[pair][0][1]
                # print("Adding char ", char, " times ", amount)
                if not counts.get(char):
                    counts[char] = amount
                else:
                    counts[char] += amount
                for new in rules[pair]:
                    if not new_polymer.get(new):
                        new_polymer[new] = amount
                    else:
                        new_polymer[new] += amount
            else:
                if not new_polymer.get(pair):
                    new_polymer[pair] = 1
                else:
                    new_polymer[pair] += 1
        polymer = new_polymer
        # print(polymer)
        # print(counts)
    
    max_count = max(counts.values())
    min_count = min(counts.values())

    result = max_count - min_count

        

    print(f"""
    If you take the quantity of the most common element
    and subtract the quantity of the least common element
    you get {result}
    """)

if __name__ == "__main__":
    main()
