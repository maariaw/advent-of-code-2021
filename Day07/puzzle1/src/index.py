from inputreader import InputReader

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day07/input.txt"
    reader = InputReader(path)
    crab_positions = reader.get_one_line_ints()
    # print(crab_positions)

    fuel_costs = {}

    low = min(crab_positions)
    high = max(crab_positions)

    for position in range(low, high + 1):
        fuel_sum = 0
        for crab in crab_positions:
            fuel_sum += abs(position - crab)
        fuel_costs[position] = fuel_sum
    
    optimal_position = min(fuel_costs.keys(), key=(lambda k: fuel_costs[k]))
    optimal_cost = fuel_costs[optimal_position]


    print(f"The optimal position to align to is {optimal_position}")
    print(f"This will cost a total of {optimal_cost} fuel")

if __name__ == "__main__":
    main()