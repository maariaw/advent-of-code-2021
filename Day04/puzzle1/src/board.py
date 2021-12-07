class Board:
    def __init__(self, list_of_rows):
        self.board = list_of_rows
        self.marks = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]
        ]

    def mark_number(self, number):
        for i in range(5):
            if number in self.board[i]:
                for j in range(5):
                    if self.board[i][j] == number:
                        self.marks[i][j] = True

    def check_win(self):
        for i in range(5):
            if all(self.marks[i]):
                return True
            column = list(map(lambda row: row[i], self.marks))
            if all(column):
                return True

    def sum_unmarked(self):
        unmarked_sum = 0
        for i in range(5):
            for j in range(5):
                    if self.marks[i][j] == 0:
                        unmarked_sum += int(self.board[i][j])
        return unmarked_sum

    def __str__(self):
        string = ""
        for row in self.board:
            for number in row:
                string += f"{str(number):2}" + " "
            string += "\n"  
        string += "\n"
        for row in self.marks:
            for number in row:
                string += f"{str(number):2}" + " "
            string += "\n"  

        return string
