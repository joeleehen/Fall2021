import sys


# Input: takes as input a positive integer n
# Output: returns True if n is prime and False otherwise
def is_prime(n):
    if n == 1:
        return False
    limit = int(n ** 0.5) + 1
    div = 2
    while div < limit:
        if n % div == 0:
            return False
        div += 1
    return True


# Input: takes as input a string in lower case and the size
#        of the hash table
# Output: returns the index the string will hash into
def hash_word(s, size):
    hash_idx = 0
    for j in range(len(s)):
        letter = ord(s[j]) - 96
        hash_idx = (hash_idx * 26 + letter) % size
    return hash_idx


# Input: takes as input a string in lower case and the constant
#        for double hashing
# Output: returns the step size for that string
def step_size(s, const):
    hash_idx = 0
    for idx in range(len(s)):
        let = ord(s[idx]) - 96
        hash_idx = const - (hash_idx * 26 + let) % const
    return hash_idx


# Input: takes as input a string and a hash table
# Output: no output; the function enters the string in the hash table,
#         it resolves collisions by double hashing
def insert_word(s, hash_table):
    first_hash = hash_word(s, len(hash_table))
    second_hash = step_size(s, 26)
    count = 0
    idx = first_hash + count * second_hash

    if hash_table[first_hash] is None:
        hash_table[first_hash] = s
    elif hash_table[first_hash] is not None:
        while hash_table[idx] is not None:
            count += 1
            idx = first_hash + count * second_hash
            mod_idx = idx % len(hash_table)
        hash_table[mod_idx] = s


# Input: takes as input a string and a hash table
# Output: returns True if the string is in the hash table
#         and False otherwise
def find_word(s, hash_table):
    hash1 = hash_word(s, len(hash_table))
    if hash_table[hash1] == s:
        return True
    else:
        i = 1
        hash2 = step_size(s, 11)
        newIdx = hash1 + (i * hash2)
        if hash_table[newIdx] == s:
            return True
        while hash_table[newIdx] != s:
            if hash_table[newIdx] == "":
                return False
            i += 1
            newIdx = hash1 + (i * hash2) % len(hash_table)
            if hash_table[newIdx] == s:
                return True

        return False


# Input: string s, a hash table, and a hash_memo
#        recursively finds if the string is reducible
# Output: if the string is reducible it enters it into the hash memo
#         and returns True and False otherwise
def is_reducible(s, hash_table, hash_memo):
    if len(s) == 1:
        if s == "a" or s == "i" or s == "o":
            return True
        return False
    elif find_word(s, hash_memo):
        return True
    elif find_word(s, hash_table):
        for i in range(len(s)):
            temp = s[:i] + s[i + 1:]
            if is_reducible(temp, hash_table, hash_memo):
                insert_word(s, hash_memo)
                return True

    return False


# Input: string_list a list of words
# Output: returns a list of words that have the maximum length
def get_longest_words(string_list):
    longest = []
    lenList = [len(word) for word in string_list]
    for i in range(len(lenList)):
        if lenList[i] == max(lenList):
            longest.append(string_list[i])
    return longest


def main():
    # create an empty word_list
    word_list = []

    # read words from words.txt and append to word_list
    for line in sys.stdin.readlines():
        line = line.strip()
        word_list.append(line)

    print("done")
    # find length of word_list
    word_list_len = len(word_list)

    # determine prime number N that is greater than twice
    # the length of the word_list
    prime_formula = word_list_len * 2 + 1
    prime = prime_formula
    while not is_prime(prime):
        prime = prime_formula + 1

    # create an empty hash_list
    hash_list = []

    # populate the hash_list with N blank strings
    for n in range(prime):
        hash_list.append('')

    # hash each word in word_list into hash_list
    # for collisions use double hashing
    for string in word_list:
        insert_word(string, hash_list)

    # create an empty hash_memo of size M
    hash_memo = []

    # we do not know a priori how many words will be reducible
    # let us assume it is 10 percent (fairly safe) of the words
    # then M is a prime number that is slightly greater than
    # 0.2 * size of word_list
    M = 0.2 * len(word_list)
    while not is_prime(M):
        M += 1

    # populate the hash_memo with M blank strings
    for i in range(M):
        hash_memo.append("")

    # create an empty list reducible_words
    reducible_words = []

    # for each word in the word_list recursively determine
    # if it is reducible, if it is, add it to reducible_words
    for word in word_list:
        if is_reducible(word, hash_list, hash_memo):
            reducible_words.append(word)

    # as you recursively remove one letter at a time check
    # first if the sub-word exists in the hash_memo. if it does
    # then the word is reducible and you do not have to test
    # any further. add the word to the hash_memo.

    # find the largest reducible words in reducible_words
    longestList = get_longest_words(reducible_words)

    # print the reducible words in alphabetical order
    # one word per line
    longestList.sort()
    for word in longestList:
        print(word)


if __name__ == "__main__":
    main()
