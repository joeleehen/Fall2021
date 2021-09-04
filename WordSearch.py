
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
    charFound = ""
    location = (0, 0)
    for i in range(len(grid) - len(word) + 1):    # ensures valid indexing
        rowExamined = grid[i]
        for j in range(len(rowExamined)):
            rowTrack = i
            if rowExamined[j] == word[0]:
                wordTrack = 0    # used to iterate within the searchword
                charFound = ""    # used to keep track of characters that match searchword
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
    if charFound != word:
        location = (0, 0)
    return location


def reverseVertSearch(grid, word):
    location = (0, 0)
    charFound = ""
    for i in range(len(grid) - 1, len(word) - 2, -1):    # iterate backwards through grid
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
    if charFound != word:
        location = (0, 0)
    else:
        pass
    return location


def bottomRightSearch(grid, word):
    charFound = ""
    location = (0, 0)
    for i in range(len(grid) - len(word) + 1):
        rowExamined = grid[i]
        for j in range(len(rowExamined) - len(word) + 1):
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
    for i in range((len(grid) - len(word) + 1)):
        rowExamined = grid[i]
        for j in range((len(word) - 1), len(rowExamined)):
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
    for i in range(len(grid) - 1, len(word) - 2, -1):
        rowExamined = grid[i]
        for j in range(len(rowExamined) - len(word) + 1):
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
    for i in range(len(grid) - 1, len(word) - 2, -1):
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
    gridSize = sys.stdin.readline()
    gridSize = int(gridSize)
    sys.stdin.readline()    # skip blank line
    gridList = getGridList(gridSize)
    sys.stdin.readline()
    wordList = getWorkBank()
    return gridList, wordList


def find_word(grid, word):
    location = horiSearch(grid, word)
    if location == (0, 0):
        location = reverseHoriSearch(grid, word)
        if location == (0, 0):
            location = vertSearch(grid, word)
            if location == (0, 0):
                location = reverseVertSearch(grid, word)
                if location == (0, 0):
                    location = bottomLeftSearch(grid, word)
                    if location == (0, 0):
                        location = bottomRightSearch(grid, word)
                        if location == (0, 0):
                            location = upperLeftSearch(grid, word)
                            if location == (0, 0):
                                location = upperRightSearch(grid, word)
    return location


def main():
    gridList, wordList = read_input()
    for word in wordList:
        location = find_word(gridList, word)
        if location == (-1, -1):    # if word isn't in grid
            location = (0, 0)
        print(word + ": " + str(location))


if __name__ == "__main__":
    main()
