import sys

# Populate a 2-D list with numbers from 1 to n2
# This function must take as input an integer. You may assume that
# n >= 1 and n is odd. This function must return a 2-D list (a list of
# lists of integers) representing the square.
# Example 1: make_square(1) should return [[1]]
# Example 2: make_square(3) should return [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
def make_square(n):
    magicSquare = []
    if n != 1:
        for i in range(n):
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

# Print the magic square in a neat format where the numbers
# are right justified. This is a helper function.
# This function must take as input a 2-D list of integers
# This function does not return any value
# Example: Calling print_square (make_square(3)) should print the output
# 4 9 2
# 3 5 7
# 8 1 6
def print_square(magic_square):
    for row in magic_square:
        for num in row:
            print(num + " ", end="")
        print()

# Check that the 2-D list generated is indeed a magic square
# This function must take as input a 2-D list, and return a boolean
# This is a helper function.
# Example 1: check_square([[1, 2], [3, 4]]) should return False
# Example 2: check_square([[4, 9, 2], [3, 5, 7], [8, 1, 6]]) should return True
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

# Input: square is a 2-D list and n is an integer
# Output: returns two integers representing the locations of n in the square
def findNumber(square, n):
    for i in range(len(square)):
        xCord = i
        rowString = "".join(square[i])
        yCord = rowString.find(str(n))
        if yCord != -1:
            break
    return xCord, yCord

# Input: square is a 2-D list and n is an integer
# Output: returns an integer that is the sum of the
#         numbers adjacent to n in the magic square
#         if n is outside the range return 0
def sum_adjacent_numbers(square, n):
    # find n in square
    numList = [i for i in range(1, (len(square) ** 2) + 1)]
    if n not in numList:
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
        if y == len(square) - 1:
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
    for line in sys.stdin():
        findMe = line
        magicSum = sum_adjacent_numbers(magicSquare, findMe)
        print(magicSum)


if __name__ == "__main__":
    main()
