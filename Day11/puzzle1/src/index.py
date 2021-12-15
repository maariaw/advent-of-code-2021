from octopusmapper import OctopusMapper
from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day11/input.txt"
    reader = InputReader(path)
    string_lines = reader.get_string_list()
    mapper = OctopusMapper(string_lines)
    steps = 100
    total_flashes = 0
    # displays = []
    # displays.append(mapper.get_display())
    for step in range(steps):
        total_flashes += mapper.do_step()
        # displays.append("\n-----------------------------------\n")
        # displays.append(f"After step {step + 1}\n\n")
        # displays.append(mapper.get_display())
    
    # with open('/home/mawahlst/Documents/Projects/AdventOfCode/Day11/puzzle1/src/output.txt', 'w') as writer:
    #     for display in displays:
    #         writer.write(str(display))


    print(f"{total_flashes} flashes happened during {steps} steps")

if __name__ == "__main__":
    main()