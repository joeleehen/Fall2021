import sys


def getGridList(gridSize):
    gridList = []
    for i in range(gridSize):
        rowStr = sys.stdin.readline()
        rowStr = rowStr.replace("\n", "")    # remove escape character
        rowLst = []
        for c in rowStr:    # create list containing letters in grid row, omit spaces
            if c != " ":
                rowLst.append(c)
        gridList.append(rowLst)
    return gridList


def getWorkBank():
    # don't forget to skip over another empty line
    numWords = int(sys.stdin.readline())
    wordList = []
    for i in range(numWords):
        wordStr = sys.stdin.readline()
        wordStr = wordStr.replace("\n", "")
        wordList.append(wordStr)
    return wordList


def horiSearch(grid, word):
    location = (0, 0)
    for i in range(len(grid)):
        rowExamined = grid[i]    # current row of grid being examined, is a list of characters!
        rowJoined = "".join(rowExamined)    # convert to string
        if rowJoined.find(word) != -1:
            location = (i + 1, rowJoined.find(word) + 1)
        else:
            continue
    return location


def reverseHoriSearch(grid, word):
    location = (0, 0)
    for i in range(len(grid)):
        rowExamined = grid[i]
        rowJoined = "".join(rowExamined)
        wordReversed = word[::-1]
        if rowJoined.find(wordReversed) != -1:
            location = (i + 1, rowJoined.find(wordReversed) + len(wordReversed))
        else:
            continue
    return location

def vertSearch(grid, word):
    location = (0, 0)
    for i in range(len(grid)):
        rowExamined = grid[i]
        for j in range(len(rowExamined)):
            rowTrack = i
            if rowExamined[j] == word[0]:
                wordTrack = 0    # used to iterate within the searchword
                charFound = ''    # used to keep track of characters that match searchword
                while wordTrack < len(word) and grid[rowTrack][j] == word[wordTrack]:
                    charFound += word[wordTrack]
                    rowTrack += 1
                    wordTrack += 1
                    location = (i + 1, j + 1)
                    if charFound == word:
                        break
                else:
                    continue
                break    # break out of while loop
            else:
                continue
        else:
            continue
        break    # break out of row iterator
    return location


def reverseVertSearch(grid, word):
    location = (0, 0)
    for i in range(13, 0, -1):    # iterate backwards through grid
        rowExamined = grid[i]
        for j in range(len(rowExamined)):
            rowTrack = i
            if rowExamined[j] == word[0]:
                wordTrack = 0  # used to iterate within the searchword
                charFound = ''  # used to keep track of characters that match searchword
                while wordTrack < len(word) and grid[rowTrack][j] == word[wordTrack]:
                    charFound += word[wordTrack]
                    rowTrack -= 1
                    wordTrack += 1
                    location = (i + 1, j + 1)
                    if charFound == word:
                        break
                else:
                    continue
                break  # break out of while loop
            else:
                continue
        else:
            continue
        break  # break out of row iterator
    return location


def bottomRightSearch(grid, word):
    charFound = ""
    location = (0, 0)
    for i in range(len(grid)):
        rowExamined = grid[i]
        for j in range(len(rowExamined)):
            rowTrack = i
            if rowExamined[j] == word[0]:
                wordTrack = 1  # iterates within the searchword
                charFound = word[0]  # keeps track of characters that match searchword
                rightTick = j + 1    # iterates to the right
                while wordTrack < len(word) and grid[rowTrack + 1][rightTick] == word[wordTrack]:
                    charFound += word[wordTrack]
                    rowTrack += 1    # iterate downwards
                    wordTrack += 1
                    location = (i + 1, j + 1)
                    rightTick += 1
                    if charFound == word:
                        break
                else:
                    continue
                break  # break out of while loop
            else:
                continue
        else:
            continue
        break  # break out of row iterator
    if charFound != word:
        location = (0, 0)
    return location


def bottomLeftSearch(grid, word):
    charFound = ""
    location = (0, 0)
    for i in range(len(grid)):
        rowExamined = grid[i]
        for j in range(len(rowExamined)):
            rowTrack = i
            if rowExamined[j] == word[0]:
                wordTrack = 1
                charFound = word[0]
                leftTick = j - 1    # iterates to the left
                while wordTrack < len(word) and grid[rowTrack + 1][leftTick] == word[wordTrack]:
                    charFound += word[wordTrack]
                    rowTrack += 1    # iterate downwards
                    wordTrack += 1
                    location = (i + 1, j + 1)
                    leftTick -= 1
                    if charFound == word:
                        break
                else:
                    continue
                break  # break out of while loop
            else:
                continue
        else:
            continue
        break  # break out of row iterator
    if charFound != word:
        location = (0, 0)
    return location


def upperRightSearch(grid, word):
    charFound = ""
    location = (0, 0)
    for i in range(13, 0, -1):
        rowExamined = grid[i]
        for j in range(len(rowExamined)):
            rowTrack = i
            if rowExamined[j] == word[0]:
                wordTrack = 1
                charFound = word[0]
                rightTick = j + 1  # iterates to the right
                while wordTrack < len(word) and grid[rowTrack - 1][rightTick] == word[wordTrack]:
                    charFound += word[wordTrack]
                    rowTrack -= 1    # iterates upwards
                    wordTrack += 1
                    location = (i + 1, j + 1)
                    rightTick += 1
                    if charFound == word:
                        break
                else:
                    continue
                break  # break out of while loop
            else:
                continue
        else:
            continue
        break  # break out of row iterator
    if charFound != word:
        location = (0, 0)
    return location

def upperLeftSearch(grid, word):
    charFound = ""
    location = (0, 0)
    for i in range(13, 0, -1):
        rowExamined = grid[i]
        for j in range(len(rowExamined)):
            rowTrack = i
            if rowExamined[j] == word[0]:
                wordTrack = 1
                charFound = word[0]
                leftTick = j - 1    # iterates to the left
                while wordTrack < len(word) and grid[rowTrack - 1][leftTick] == word[wordTrack]:
                    charFound += word[wordTrack]
                    rowTrack -= 1    # iterates upwards
                    wordTrack += 1
                    location = (i + 1, j + 1)
                    leftTick -= 1
                    if charFound == word:
                        break
                else:
                    continue
                break  # break out of while loop
            else:
                continue
        else:
            continue
        break  # break out of row iterator
    if charFound != word:
        location = (0, 0)
    return location


def read_input():
    # gridSize = sys.stdin.readline()
    f = open(r"C:\Users\Joey\Fall2021\word_grid.in.txt", "r")    # FIXME
    gridSize = (f.readline())     # FIXME
    # gridList = getGridList(gridSize)
    gridList = []     # FIXME
    for i in range(int(gridSize)):    # FIXME
        rowStr = f.readline()    # FIXME
        rowStr = rowStr.replace("\n", "")  # FIXME
        rowLst = []    # FIXME
        for c in rowStr:  # FIXME
            if c != " ":    # FIXME
                rowLst.append(c)    # FIXME
        gridList.append(rowLst)    # FIXME
    f.readline()    # FIXME
    # sys.stdin.readline()
    numWords = (f.readline())    # FIXME
    wordList = []    # FIXME
    for i in range(int(numWords)):    # FIXME
        wordStr = f.readline()    # FIXME
        wordStr = wordStr.replace("\n", "")    # FIXME
        wordList.append(wordStr)    # FIXME
    # wordList = getWorkBank()
    return gridList, wordList


def find_word(grid, word):
    location = (0, 0)
    while location == (0, 0):
        location = horiSearch(grid, word)
        location = reverseHoriSearch(grid, word)
        location = vertSearch(grid, word)
        location = reverseVertSearch(grid, word)
        location = bottomRightSearch(grid, word)
        location = bottomLeftSearch(grid, word)
        location = upperRightSearch(grid, word)
        location = upperLeftSearch(grid, word)
        location = (-1, -1)    # breaks loop while still showing word isn't in grid
    return location


def main():
    gridList, wordList = read_input()
    for word in wordList:
        loc_found = find_word(gridList, word)
        if loc_found == (-1, -1):    # if word isn't in grid
            loc_found = (0, 0)
        else:
            continue
        print(word + ": " + str(loc_found))


if __name__ == "__main__":
    main()
