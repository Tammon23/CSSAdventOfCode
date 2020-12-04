# o(n) solution
import re


# using regex to check if certain fields exist in a given string
# and if those fields are valid
# in a fast (not very readable) way
def checkstring(s):
    byr = iyr = eyr = hgt = hcl = ecl = pid = 0
    if "byr:" in s:
        byr = 1
    if "iyr:" in s:
        iyr = 1
    if "eyr:" in s:
        eyr = 1
    if "hgt:" in s:
        hgt = 1
    if "hcl:" in s:
        hcl = 1
    if "ecl:" in s:
        ecl = 1
    if "pid:" in s:
        pid = 1

    return byr, iyr, eyr, hgt, hcl, ecl, pid


# given a list of passports
# counts how many are valid
def numValid(passports):
    numValids = 0
    score = [0, 0, 0, 0, 0, 0, 0]
    for row in passports:
        if row != "\n":
            score = [i if i else score[v] for v, i in enumerate(checkstring(row))]
            continue

        elif sum(score) == 7:
            numValids += 1
        score = [0, 0, 0, 0, 0, 0, 0]

    else:
        if sum([i if i else score[v] for v, i in enumerate(checkstring(row))]) == 7:
            numValids += 1

    return numValids


if __name__ == "__main__":
    inputs = []

    # reading in the input
    with open("../input.txt", "r") as f:
        inputs = f.readlines()

    print(numValid(inputs))

# ALWAYS CHECK THE LAST LINE