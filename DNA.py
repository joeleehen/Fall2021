#   File: DNA.py

#   Description: Reads in a pair of DNA strings and searches for the longest common contiguous subsequence

#   Student Name: Deborah Lin

#   Student UT EID: dl34755

#   Partner Name: Joseph Hendrix

#   Partner UT EID: jlh7459

#   Course Name: CS 313E

#   Unique Number: 52595

#   Date Created: August 27, 2021

#   Date Last Modified: August 29, 2021

#   Input: s1 and s2 are two strings that represent strands of DNA

#   Output: returns a sorted list of substrings that are the longest 
#         common subsequence. The list is empty if there are no 
#         common subsequences.
def longest_subsequence(s1, s2):
    answer = ""
    len1, len2 = len(s1), len(s2)
    for i in range(len1):
        for j in range(len2):
            lcs_temp = 0    # used to iterate across strings once common character is found
            match = ''
            # while loop to check for matchness and validity of index
            while i + lcs_temp < len1 and j + lcs_temp < len2 and s1[i + lcs_temp] == s2[j + lcs_temp]:
                match += s2[j + lcs_temp]
                lcs_temp += 1
            # replace answer with longest match found
            if len(match) > len(answer):
                answer = match
    return answer


def PrintAndClean(seq):
    if len(seq) == 1 and "\n" not in seq:    # ensures that \n isn't valid answer
        print("\n" + seq[0])

    elif len(seq) > 1 and "" not in seq:
        # sort elements of list alphabetically
        seq.sort()
        print("")
        for x in seq:
            print(x)

    else:
        print("\n" + "No Common Sequence Found")


def main():
    # read the data
    import sys
    pairs = int(sys.stdin.readline())
    # for each pair
    for i in range(pairs):
        s1 = sys.stdin.readline()
        s2 = sys.stdin.readline()
        s1 = s1.upper()
        s2 = s2.upper()

        sequences = []    # list of sequences found
        # call longest subsequences
        answer = longest_subsequence(s1, s2)
        sequences.append(answer)

        while (len(answer) < len(s2)) and (len(answer) < len(s1)):
            # string 1
            # indexes where longest common sequence is
            help1 = int(s1.find(answer)) + len(answer)
            i = help1
            new1 = ""
            # splits string from longest common sequence
            while i < len(s1):
                new1 = new1 + s1[i]
                i += 1
            s1 = new1
            # repeats first part for string 2
            help2 = int(s2.find(answer)) + len(answer)
            i = help2
            new2 = ""
            while i < len(s2):
                new2 = new2 + s2[i]
                i += 1
            s2 = new2
            # runs function again to find the second longest common sequence
            answer1 = longest_subsequence(s1, s2)
            # tests to see if it is the same length as the longest common sequence
            if len(answer1) == len(answer):
                sequences.append(answer1)

    # write out result(s)
        PrintAndClean(sequences)
    print("")


if __name__ == "__main__":
    main()
