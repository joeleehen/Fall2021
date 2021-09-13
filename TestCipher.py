import sys

#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is encoded with
#          rail fence algorithm
def rail_fence_encode(strng, key):
    railFence = []
    for i in range(key):
        railFence.append(["-" for i in range(len(strng))])    # create 'empty' list
    goingDown = True    # used to zigzag through the rail matrix
    x, y = 0, 0
    for c in strng:
        railFence[x][y] = c
        y += 1
        if x == key - 1:
            goingDown = False
        elif x == 0:
            goingDown = True

        if goingDown:
            x += 1
        else:
            x -= 1
    # find encrypted string
    encryptedText = ""
    for row in railFence:
        for c in row:
            if c.isalpha():
                encryptedText += c
    return encryptedText


#  Input: strng is a string of characters and key is a positive
#         integer 2 or greater and strictly less than the length
#         of strng
#  Output: function returns a single string that is decoded with
#          rail fence algorithm
def rail_fence_decode(strng, key):
    railFence = []
    for i in range(key):
        railFence.append(["-" for i in range(len(strng))])  # create 'empty' list
    goingDown = True    # zigzags through rail
    x, y = 0, 0
    # place an x where a letter should appear
    for i in range(len(strng)):
        railFence[x][y] = "x"
        y += 1
        if x == key - 1:
            goingDown = False
        elif x == 0:
            goingDown = True

        if goingDown:
            x += 1
        else:
            x -= 1
    # replace x with letter in string
    stringTrack = 0    # used to track index within encrypted text
    for x in range(len(railFence)):
        for y in range(len(strng)):
            if railFence[x][y].isalpha():
                railFence[x][y] = strng[stringTrack]
                stringTrack += 1
    # read decrypted text
    decryptedText = ""
    goingDown = True
    x, y = 0, 0
    # zigzag through rail fence, collecting letters as they appear
    for i in range(len(strng)):
        if railFence[x][y].isalpha():
            decryptedText += railFence[x][y]
        y += 1
        if x == key - 1:
            goingDown = False
        elif x == 0:
            goingDown = True

        if goingDown:
            x += 1
        else:
            x -= 1
    return decryptedText
# TODO: IMPLEMENT VIGENERE CIPHER

#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
  return ""	   # placeholder for the actual return statement
