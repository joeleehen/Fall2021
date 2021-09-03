import sys

# gridSize = int(sys.stdin.readline())

file = open(r"/Users/josephhendrix/Fall2021/word_grid.in.txt", "r")
gridSize = int(file.readline())    # USED FOR TESTING
file.readline()    # skip over empty line


def getGridList(gridSize):
    gridList = []
    for i in range(gridSize):
        rowStr = file.readline()
        rowStr = rowStr.replace("\n", "")    # remove escape character
        rowLst = []
        for c in rowStr:    # create list containing letters in grid row, omit spaces
            if c != " ":
                rowLst.append(c)
        gridList.append(rowLst)
    return gridList


def getWorkBank():
    # don't forget to skip over another empty line
    numWords = int(file.readline())
    wordList = []
    for i in range(numWords):
        wordStr = file.readline()
        wordStr = wordStr.replace("\n", "")
        wordList.append(wordStr)
    return wordList


gridList = getGridList(gridSize)
file.readline()    # skip over blank line again
wordList = getWorkBank()


def horiSearch(word):
    location = (0, 0)
    for i in range(len(gridList)):
        rowExamined = gridList[i]    # current row of grid being examined, is a list of characters!
        rowJoined = "".join(rowExamined)    # convert to string
        if rowJoined.find(word) != -1:
            location = (i + 1, rowJoined.find(word) + 1)
        else:
            continue
    return location


def reverseHoriSearch(word):
    location = (0, 0)
    for i in range(len(gridList)):
        rowExamined = gridList[i]
        rowJoined = "".join(rowExamined)
        wordReversed = word[::-1]
        if rowJoined.find(wordReversed) != -1:
            location = (i + 1, rowJoined.find(wordReversed) + len(wordReversed))
        else:
            continue
    return location

def vertSearch(word):
    location = (0, 0)
    for i in range(len(gridList)):
        rowTrack = i    # used to iterate rows after initial match is found
        rowExamined = gridList[i]
        for j in range(len(rowExamined)):
            if rowExamined[j] == word[0]:
                rowFound = i    # denotes first row where word is found
                wordTrack = 0    # used to iterate within the searchword
                charFound = ''    # used to keep track of characters that match searchword
                while wordTrack < len(word) and gridList[rowTrack][j] == word[wordTrack]:
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


print(vertSearch("BOOTS"))

# HERE'S THE PLAN
# Each search function is based off of the first letter in the searchword.

# Diagonal search is a combination of the two. Use indexing and for loops to iterate
# through each row and index.

# Remember to repeat these processes in the reverse. That should be easy, just redefine each function
# but in the opposite direction


# Throw all of these search functions into a finder function find_word(grid, word). Remove each searchword from
# the list as it's found. Feeling pretty confident about this shit bro!
