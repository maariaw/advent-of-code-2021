from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day14/input.txt"
    reader = InputReader(path)
    data = reader.get_split_lines_by_separator(" -> ")
    template = data[0][0]
    pairs = [(pair[0], pair[1]) for pair in data if len(pair) > 1]
    rules = {}
    for pair in list(filter(lambda line: len(line) > 1, pairs)):
        rules[pair[0]] = pair[1]

    steps = 10
    
    for step in range(steps):
        new_template = ""
        for i in range(len(template) - 1):
            new_template += template[i]
            pair = template[i:i+2]
            if pair in rules:
                new_template += rules[pair]
            # print(new_template)
        new_template += template[-1]
        # print(new_template)
        template = new_template

    counts = []
    counted = set()
    for char in template:
        if char in counted:
            continue
        counted.add(char)
        counts.append(template.count(char))
    
    max_count = max(counts)
    min_count = min(counts)

    result = max_count - min_count

        

    print(f"""
    If you take the quantity of the most common element
    and subtract the quantity of the least common element
    you get {result}
    """)

if __name__ == "__main__":
    main()
