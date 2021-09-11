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
        magicSquare[-2][n // 2] = int(1)

        # populate square
        startX = n - 1
        startY = n // 2
        for nextNum in numList:
            startX += 1
            if magicSquare[startX][startY] == "invalid":
                startX = 0
            startY += 1
            magicSquare[startX][startY] = nextNum



        print(magicSquare)


make_square(3)
