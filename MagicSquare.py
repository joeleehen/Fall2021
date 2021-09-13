
import sys


def make_square(n):
    magicSquare = []
    n = int(n)
    if n != 1:
        for i in range(int(n)):
            magicSquare.append(["x" for i in range(n)])    # makes empty row list
        for i in range(n):
            magicSquare[i].append("invalid")
        magicSquare.append(["invalid" for i in range(n)])
        magicSquare[-1].append("corner")
        numList = [i for i in range(2, (n ** 2 + 1))]    # makes a list of numbers to appear in square
        # place 1 in square
        magicSquare[-2][n // 2] = str(1)

        # populate square
        startX = n - 1
        startY = n // 2
        for nextNum in numList:
            startX += 1
            startY += 1
            if magicSquare[startX][startY] == "corner":    # move above original num if on invalid corner
                startX -= 2
                startY -= 1
            if startX >= n:    # restart on other side if "out of range"
                startX = 0
            if startY >= n:
                startY = 0
            # if there's already a num in that cell, move above the original num
            if magicSquare[startX][startY].isnumeric():
                startX -= 2
                startY -= 1
            magicSquare[startX][startY] = str(nextNum)

        # clean square
        magicSquare.pop()
        for row in magicSquare:
            row.pop()

        return magicSquare


def print_square(magic_square):
    for row in magic_square:
        for num in row:
            print(str(num), end=" ")
        print()


def check_square(magic_square):
    magicSum = len(magic_square) * ((len(magic_square) ** 2) + 1) // 2
    for row in magic_square:    # check the rows
        checkSum = 0
        for num in row:
            checkSum += int(num)
        if checkSum != magicSum:
            return False
    for i in range(len(magic_square[0])):    # check columns
        checkSum = 0
        for row in magic_square:
            checkSum += int(row[i])
        print(checkSum)
        if checkSum != magicSum:
            return False
    yCord = 0    # check diagonals
    checkSum = 0
    for xCord in range(len(magic_square)):
        checkSum += int(magic_square[xCord][yCord])
        yCord += 1
    if checkSum != magicSum:
        return False

    return True


def findNumber(square, n):
    for i in range(len(square)):
        xCord = i
        try:
            yCord = square[i].index(str(n))
        except ValueError:
            yCord = -1
        if yCord != -1:
            break
    return xCord, yCord


def sum_adjacent_numbers(square, n):
    # find n in square
    numList = [i for i in range(1, (len(square) ** 2) + 1)]
    if int(n) not in numList:
        adjSum = 0
    else:
        adjSum = 0
        x, y = findNumber(square, n)
        if y == 0:
            if x == 0:
                # add right, bottom 2
                adjSum += int(square[x][y + 1])
                adjSum += int(square[x + 1][y])
                adjSum += int(square[x + 1][y + 1])
            elif x == len(square) - 1:
                # add top 2, right
                adjSum += int(square[x - 1][y])
                adjSum += int(square[x - 1][y + 1])
                adjSum += int(square[x][y + 1])
            else:
                # add top 2, right, bottom 2
                adjSum += int(square[x - 1][y])
                adjSum += int(square[x - 1][y + 1])
                adjSum += int(square[x][y + 1])
                adjSum += int(square[x + 1][y])
                adjSum += int(square[x + 1][y + 1])
        elif y == len(square) - 1:
            if x == 0:
                # add left, bottom 2
                adjSum += int(square[x][y - 1])
                adjSum += int(square[x + 1][y])
                adjSum += int(square[x + 1][y - 1])
            elif x == len(square) - 1:
                # add top 2, left
                adjSum += int(square[x - 1][y])
                adjSum += int(square[x - 1][y - 1])
                adjSum += int(square[x][y - 1])
            else:
                # add top 2, left, bottom 2
                adjSum += int(square[x - 1][y - 1])
                adjSum += int(square[x - 1][y])
                adjSum += int(square[x][y - 1])
                adjSum += int(square[x + 1][y - 1])
                adjSum += int(square[x + 1][y])
        elif x == 0:
            # add sides, bottom 3
            adjSum += int(square[x][y - 1])
            adjSum += int(square[x][y + 1])
            adjSum += int(square[x + 1][y - 1])
            adjSum += int(square[x + 1][y])
            adjSum += int(square[x + 1][y + 1])
        elif x == len(square) - 1:
            # top 3, sides
            adjSum += int(square[x - 1][y - 1])
            adjSum += int(square[x - 1][y])
            adjSum += int(square[x - 1][y + 1])
            adjSum += int(square[x][y - 1])
            adjSum += int(square[x][y + 1])
        else:
            # add top 3, sides, bottom 3
            adjSum += int(square[x - 1][y - 1])
            adjSum += int(square[x - 1][y])
            adjSum += int(square[x - 1][y + 1])
            adjSum += int(square[x][y - 1])
            adjSum += int(square[x][y + 1])
            adjSum += int(square[x + 1][y - 1])
            adjSum += int(square[x + 1][y])
            adjSum += int(square[x + 1][y + 1])
    return adjSum


def main():
    # read input file from stdin
    size = sys.stdin.readline()
    # create magic square
    magicSquare = make_square(size)
    # print the sum of the adjacent numbers
    for line in map(str.rstrip, sys.stdin):
        findMe = line
        magicSum = sum_adjacent_numbers(magicSquare, findMe)
        print(magicSum)


if __name__ == "__main__":
    main()
