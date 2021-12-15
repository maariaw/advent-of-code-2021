from octopusmapper import OctopusMapper
from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day11/input.txt"
    reader = InputReader(path)
    string_lines = reader.get_string_list()
    mapper = OctopusMapper(string_lines)
    current_step = 1
    # displays = []
    # displays.append(mapper.get_display())
    while not mapper.do_step():
        current_step += 1
        # displays.append("\n-----------------------------------\n")
        # displays.append(f"After step {step + 1}\n\n")
        # displays.append(mapper.get_display())
    
    # with open('/home/mawahlst/Documents/Projects/AdventOfCode/Day11/puzzle1/src/output.txt', 'w') as writer:
    #     for display in displays:
    #         writer.write(str(display))


    print(f"All dumbo octopi synchronized on step {current_step}")

if __name__ == "__main__":
    main()