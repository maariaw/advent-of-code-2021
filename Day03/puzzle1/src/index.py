from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day03/input.txt"
    reader = InputReader(path)
    binaries = reader.get_string_list()
    # binaries = [
    #     "00100",
    #     "11110",
    #     "10110",
    #     "10111",
    #     "10101",
    #     "01111",
    #     "00111",
    #     "11100",
    #     "10000",
    #     "11001",
    #     "00010",
    #     "01010"
    # ]

    gamma = ""
    epsilon = ""
    for bit in range(len(binaries[0])):
        list_of_bits = []
        for binary in binaries:
            list_of_bits.append(binary[bit])
        gamma_bit = max(list_of_bits, key=list_of_bits.count)
        epsilon_bit = str(1 - int(gamma_bit))
        gamma += gamma_bit
        epsilon += epsilon_bit
    
    power_consumption = int(gamma, 2) * int(epsilon, 2)

    print("Submarine power consumption is ", power_consumption)


if __name__ == "__main__":
    main()