#  File: Chess.py

#  Description:

#  Student Name: Joseph Hendrix

#  Student UT EID: jlh7459

#  Partner Name:

#  Partner UT EID:

#  Course Name: CS 313E

#  Unique Number: 52595

#  Date Created: 10/17/21

#  Date Last Modified: TODO: update

import sys


class Queens(object):

    def __init__(self, n=8):
        self.board = []
        self.n = n
        self.solutions = []    # list of solutions, will be checked for duplicates
        for i in range(self.n):
            row = []
            for j in range(self.n):
                row.append('*')
            self.board.append(row)

    # print the board
    def print_board(self):
        for i in range(self.n):
            for j in range(self.n):
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

    # do the recursive backtracking
    def recursive_solve(self, col, backIdx):
        if col == self.n:
            self.solutions.append(self.board)
            self.board[backIdx][col - 1] = "*"
            #return True
        else:
            for i in range(self.n):
                if self.is_valid(i, col):
                    self.board[i][col] = 'Q'

                    if self.recursive_solve(col + 1, i):
                        # return True
                        continue
                    self.board[i][col] = '*'    # backtrack here if invalid queen placement
            return False

    # if the problem has a solution print the board
    def solve(self):
        for i in range(self.n):
            if self.recursive_solve(i, self.n):
                self.print_board()

def main():
    # read the size of the board
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create a chess board
    game = Queens(n)

    # place the queens on the board and count the solutions
    game.solve()
    # print the number of solutions
    print(len(game.solutions))
    for sol in game.solutions:
        print(sol)


if __name__ == "__main__":
    main()
