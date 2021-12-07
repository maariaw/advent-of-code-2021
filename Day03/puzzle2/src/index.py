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

    oxygen_rating = find_oxygen_rating(binaries, 0)
    co2_scrubber_rating = find_co2_scrubber_rating(binaries, 0)
    
    life_support_rating = int(oxygen_rating, 2) * int(co2_scrubber_rating, 2)

    print("Submarine oxygen generator rating is ", oxygen_rating)
    print("Submarine CO2 scrubber rating is ", co2_scrubber_rating)
    print("Submarine life support rating is ", life_support_rating)

def find_oxygen_rating(binary_list, bit):
    if bit == len(binary_list[0]):
        return None
    (one_bit, zero_bit) = split_by_bit(binary_list, bit)
    if len(zero_bit) > len(one_bit):
        if len(zero_bit) == 1:
            return zero_bit[0]
        return find_oxygen_rating(zero_bit, bit + 1)
    else:
        if len(one_bit) == 1:
            return one_bit[0]
        return find_oxygen_rating(one_bit, bit + 1)

def find_co2_scrubber_rating(binary_list, bit):
    if bit == len(binary_list[0]):
        return None
    (one_bit, zero_bit) = split_by_bit(binary_list, bit)
    if len(zero_bit) <= len(one_bit):
        if len(zero_bit) == 1:
            return zero_bit[0]
        return find_co2_scrubber_rating(zero_bit, bit + 1)
    else:
        if len(one_bit) == 1:
            return one_bit[0]
        return find_co2_scrubber_rating(one_bit, bit + 1)


def split_by_bit(binary_list, bit):
    one_bit = []
    zero_bit = []
    for binary in binary_list:
        if binary[bit] == "1":
            one_bit.append(binary)
        else:
            zero_bit.append(binary)
    return (one_bit, zero_bit)

if __name__ == "__main__":
    main()