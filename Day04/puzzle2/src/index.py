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

    last_winning_board = None
    winning_number = None

    for number in drawn_numbers:
        unwon_boards = [board for board in boards if not board.won]
        if not unwon_boards:
            break
        winning_number = number
        for board in unwon_boards:
            board.mark_number(number)
            if board.check_win():
                last_winning_board = board
    

    with open('/home/mawahlst/Documents/Projects/AdventOfCode/Day04/puzzle2/src/output.txt', 'w') as writer:
        for board in boards:
            writer.write(str(board))
            writer.write("\n-----------------------------------\n")
    
    print("\nLast winning board:\n")
    print(last_winning_board)

    score_sum = last_winning_board.sum_unmarked()
    print("Sum of unmarked numbers is ", score_sum)
    print("Winning call was ", winning_number)
    print("Final score: ", score_sum * int(winning_number))

if __name__ == "__main__":
    main()
