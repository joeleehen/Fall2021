#  File: TestCipher.py

#  Description: The program will encrypt and decrypt a given
#               phrase (using provided parameters) from an
#               input file using a rail fence and Vigenere
#               cipher respectively

#  Student's Name: Joseph Hendrix

#  Student's UT EID: jlh7459

#  Partner's Name:

#  Partner's UT EID:

#  Course Name: CS 313E

#  Unique Number: 52595

#  Date Created: 9/12/13

#  Date Last Modified: 9/13/13

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
            if c != "-":
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
        if railFence[x][y] != "-":
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


#  Input: strng is a string of characters
#  Output: function converts all characters to lower case and then
#          removes all digits, punctuation marks, and spaces. It
#          returns a single string with only lower case characters
def filter_string(strng):
    punc = "!\"#$%&'()*+, -./:;<=>?@[\]^_`{|}~"
    strng = strng.lower()
    # remove numbers and punctuation from string
    for c in strng:
        if c in punc or c.isnumeric():
            strng = strng.replace(c, "")
    return strng


# Input: string is the filtered string to be decoded, phrase is the
#        pass phrase to use
# Output: function returns a string representing the keystream,
#         repeated to match the length of the filtered string
def genPassPhrase(string, phrase):
    keystream = ""
    phraseTrack = 0
    for i in range(len(string)):
        if phraseTrack >= len(phrase):    # loop through key to make keystream
            phraseTrack = 0
        keystream += phrase[phraseTrack]
        phraseTrack += 1
    return keystream


#  Input: p is a character in the pass phrase and s is a character
#         in the plain text
#  Output: function returns a single character encoded using the
#          Vigenere algorithm. You may not use a 2-D list
def encode_character(p, s):
    numP = ord(p) - 96    # convert ASCII values to easier numbers
    numS = ord(s) - 96    # example: 'a' = 1
    numCode = numP + numS - 1
    while numCode > 26:    # ensures valid alpha character
        numCode -= 26
    return chr(numCode + 96)


#  Input: p is a character in the pass phrase and s is a character
#         in the encrypted text
#  Output: function returns a single character decoded using the
#          Vigenere algorithm. You may not use a 2-D list
def decode_character(p, s):
    numP = ord(p) - 96
    numS = ord(s) - 96
    numPlain = numS - numP + 1
    while numPlain <= 0:
        numPlain += 26
    return chr(numPlain + 96)


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is encoded with
#          Vigenere algorithm
def vigenere_encode(strng, phrase):
    passPhrase = genPassPhrase(strng, phrase)
    cipher = ""
    for i in range(len(strng)):
        cipher += encode_character(passPhrase[i], strng[i])
    return cipher


#  Input: strng is a string of characters and phrase is a pass phrase
#  Output: function returns a single string that is decoded with
#          Vigenere algorithm
def vigenere_decode(strng, phrase):
    passPhrase = genPassPhrase(strng, phrase)
    cipher = ""
    for i in range(len(strng)):
        cipher += decode_character(passPhrase[i], strng[i])
    return cipher


def main():
    # read the plain text from stdin
    string = sys.stdin.readline()
    # read the key from stdin
    key = int(sys.stdin.readline())
    # encrypt and print the encoded text using rail fence cipher
    fenceCipher = rail_fence_encode(string, key)
    print("Rail Fence Cipher")
    print()
    print("Plain Text:", string)
    print("Key:", str(key))
    print("Encoded Text:", fenceCipher)
    # read encoded text from stdin
    string = sys.stdin.readline()
    # read the key from stdin
    key = int(sys.stdin.readline())
    # decrypt and print the plain text using rail fence cipher
    fenceDecipher = rail_fence_decode(string, key)
    print()
    print("Encoded Text:", string)
    print("Key:", str(key))
    print("Decoded Text:", fenceDecipher)
    print()
    # read the plain text from stdin
    stringDirty = sys.stdin.readline()
    stringClean = filter_string(stringDirty)
    # read the pass phrase from stdin
    passDirty = sys.stdin.readline()
    passClean = filter_string(passDirty)
    # encrypt and print the encoded text using Vigenere cipher
    vigenereCipher = vigenere_encode(stringClean, passClean)
    print("Vigenere Cipher")
    print()
    print("Plain Text:", stringClean)
    print("Pass Phrase:", passClean)
    print("Encoded Text:", vigenereCipher)
    # read the encoded text from stdin
    stringDirty = sys.stdin.readline()
    stringClean = filter_string(stringDirty)
    # read the pass phrase from stdin
    passDirty = sys.stdin.readline()
    passClean = filter_string(passDirty)
    # decrypt and print the plain text using Vigenere cipher
    vigenereDecipher = vigenere_decode(stringClean, passClean)
    print("")
    print("Encoded Text:", stringClean)
    print("Pass Phrase:", passClean)
    print("Decoded Text:", vigenereDecipher)
