# Partner work with Kalab Alemu

import sys


class Queens(object):
    def __init__(self, n=8):
        self.board = []
        self.n = n
        self.all_boards = []
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def __str__(self):
        for i in range(len(self.all_boards)):
            for j in range(len(self.all_boards)):
                print(self.board[i][j], end=' ')
            print()
        print()

    # check if a position on the board is valid
    def is_valid(self, row, col):
        for i in range(self.n):
            if (self.board[row][i] == 'Q') or (self.board[i][col] == 'Q'):
                return False
        for i in range(self.n):
            for j in range(self.n):
                row_diff = abs(row - i)
                col_diff = abs(col - j)
                if (row_diff == col_diff) and (self.board[i][j] == 'Q'):
                    return False
        return True

    # do the recursive backtracking # if the problem has a solution print the board
    def recursive_solve(self, col):
        if col == self.n:
            return self.solve()
        else:
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'
                    if self.recursive_solve(col + 1):
                        return True
                    self.board[i][col] = '*'
            return False

    def solve(self):
        for j in range(self.n):
            for i in range(self.n):
                appendMe = self.board[i][j]
        self.all_boards.append(appendMe)


def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create a chess board
    game = Queens(n)

    # place the queens on the board and count the solutions
    game.recursive_solve(0)

    # print the number of solutions
    print(len(game.all_boards))


if __name__ == "__main__":
    main()
