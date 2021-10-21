# Pair programming with Kalab Alemu

import sys

from timeit import timeit


# returns the greatest path sum using exhaustive search
def brute_force_help(grid, sumlist, tot, row, col):
    if row == len(grid):    # base case: if we're at the bottom of triangle
        sumlist.append(tot)
    else:
        tot += grid[row][col]
        # 'iterate' through all paths
        brute_force_help(grid, sumlist, tot, row + 1, col)
        brute_force_help(grid, sumlist, tot, row + 1, col + 1)


def brute_force(grid):
    sumList = []
    brute_force_help(grid, sumList, 0, 0, 0)
    # print(sumList)
    return max(sumList)


# returns the greatest path sum using greedy approach


def greed_help(grid, row, col):
    # base case if all rows have been checked
    if row >= len(grid):
        return 0
    # if the current num in that column is greater than the next
    elif grid[row][col] < grid[row][col + 1]:
        # add that value to mem, then go to the current numbers next row
        return grid[row][col + 1] + greed_help(grid, row + 1, col + 1)

    # if number is lower then next num
    elif grid[row][col] > grid[row][col + 1]:
        # then add the next number to mem, then goes to the next num's row
        return grid[row][col] + greed_help(grid, row + 1, col)


def greedy(grid):
    final = grid[0][0] + greed_help(grid, 1, 0)
    return final


# returns the greatest path sum using divide and conquer (recursive) approach
def div_and_conquer_help(grid, row, col, tot):
    # base case; reached the end of the triangle
    if row >= len(grid):
        return [tot]
    elif row == len(grid) - 1:
        tot = tot + grid[row][col]
        return div_and_conquer_help(grid, row + 1, col, tot)
    elif row != len(grid) - 1:
        tot = tot + grid[row][col]
        return div_and_conquer_help(grid, row + 1, col, tot) + div_and_conquer_help(grid, row + 1, col + 1, tot)


def divide_conquer(grid):
    return max(div_and_conquer_help(grid, 0, 0, 0))


# returns the greatest path sum and the new grid using dynamic programming
def dynamic_prog(grid):
    zeroIndex = 0
    for i in range(len(grid) - 2, -1, -1):
        zeroIndex += 1    # used to ignore zeros in the grid
        for num in range(len(grid[i]) - zeroIndex):
            addMe = max(grid[i + 1][num], grid[i + 1][num + 1])
            grid[i][num] += addMe
    return grid[0][0]


# reads the file and returns a 2-D list that represents the triangle
def read_file():
    # read number of lines
    line = sys.stdin.readline()
    line = line.strip()
    n = int(line)

    # create an empty grid with 0's
    grid = [[0 for i in range(n)] for j in range(n)]

    # read each line in the input file and add to the grid
    for i in range(n):
        line = sys.stdin.readline()
        line = line.strip()
        row = line.split()
        row = list(map(int, row))
        for j in range(len(row)):
            grid[i][j] = grid[i][j] + row[j]

    return grid


def main():
    # read triangular grid from file
    grid = read_file()

    """
    # check that the grid was read in properly
    print (grid)
    """

    # output greatest path from exhaustive search
    times = timeit('brute_force({})'.format(grid), 'from __main__ import brute_force', number=10)
    times = times / 10
    # print time taken using exhaustive search
    print('The greatest path sum through exhaustive search is', brute_force(grid))
    print('The time taken for exhaustive search in seconds is', times)

    # output greatest path from greedy approach
    times = timeit('greedy({})'.format(grid), 'from __main__ import greedy', number=10)
    times = times / 10
    # print time taken using greedy approach
    print('The greatest path sum through greedy search is', greedy(grid))
    print('The time taken for greedy approach in seconds is', times)

    # output greatest path from divide-and-conquer approach
    times = timeit('divide_conquer({})'.format(grid), 'from __main__ import divide_conquer', number=10)
    times = times / 10
    # print time taken using divide-and-conquer approach
    print('The greatest path sum through recursive search is', divide_conquer(grid))
    print('The time taken for recursive search in seconds is', times)

    # output greatest path from dynamic programming
    times = timeit('dynamic_prog({})'.format(grid), 'from __main__ import dynamic_prog', number=10)
    times = times / 10
    # print time taken using dynamic programming
    print('The greatest path sum through dynamic programming is', dynamic_prog(grid))
    print('The time taken for dynamic programming in seconds is', times)


if __name__ == "__main__":
    main()
