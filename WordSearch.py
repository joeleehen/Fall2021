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
        rowLst = [rowStr]
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


# HERE'S THE PLAN
# Each search function is based off of the first letter in the searchword.

# Horizontal search is straightforward: for each word, look for that word
# in each row. Could even use .find()

# Vertical search is a bit harder. If word[0] is found at gridRow[0], go to the
# next row at the same index and see if it has word[1].

# Diagonal search is a combination of the two. Use indexing and for loops to iterate
# through each row and index.

# Remember to repeat these processes in the reverse. That should be easy, just redefine each function
# but in the opposite direction


# Throw all of these search functions into a finder function find_word(grid, word). Remove each searchword from
# the list as it's found. Feeling pretty confident about this shit bro!