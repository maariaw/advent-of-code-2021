from inputreader import InputReader
from board import Board

def main():
    path = "/home/mawahlst/Documents/Projects/AdventOfCode/Day04/input.txt"
    reader = InputReader(path)
    list_of_lines_as_lists = reader.get_list_of_lists()

    drawn_numbers = list_of_lines_as_lists[0][0].split(",")
    
    boards = []

    end = len(list_of_lines_as_lists)
    for line in range(2, end, 6):
        board_lists = list_of_lines_as_lists[line:line + 5]
        boards.append(Board(board_lists))

    winning_board = None
    winning_number = None

    for number in drawn_numbers:
        winning_number = number
        for board in boards:
            board.mark_number(number)
            if board.check_win():
                winning_board = board
        if winning_board:
            break

    with open('/home/mawahlst/Documents/Projects/AdventOfCode/Day04/puzzle1/src/output.txt', 'w') as writer:
        for board in boards:
            writer.write(str(board))
            writer.write("\n-----------------------------------\n")

    print("\nWinning board:\n")
    print(winning_board)
    score_sum = winning_board.sum_unmarked()
    print("Sum of unmarked numbers is ", score_sum)
    print("Winning call was ", winning_number)
    print("Final score: ", score_sum * int(winning_number))

if __name__ == "__main__":
    main()
