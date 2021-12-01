
import re

# using regex to check if certain fields exist in a given string
# and if those fields are valid
# in a fast (not very readable) way
def checkstring(s):
    byr = iyr = eyr = hgt = hcl = ecl = pid = 0
    t = re.findall("byr:[0-9]+[ |\n|$]", s)
    if len(t) == 1 and "byr:1920" <= t[0].rstrip() <= "byr:2002":
        byr = 1

    t = re.findall("iyr:[0-9]+[ |\n]", s)
    if len(t) == 1 and "iyr:2010" <= t[0].rstrip() <= "iyr:2020":
        iyr = 1

    t = re.findall("eyr:[0-9]+[ |\n]", s)
    if len(t) == 1 and "eyr:2020" <= t[0].rstrip() <= "eyr:2030":
        eyr = 1

    t = re.findall("hgt:[0-9a-z]+[cm|in][ |\n]", s)
    if len(t) == 1:
        # t2 = next(re.finditer("[0-9]+", t[0])).group()
        ts = t[0].rstrip().rstrip("cm").rstrip("in")
        if "cm" in t[0] and "hgt:150" <= ts <= "hgt:193" or "in" in t[0] and "hgt:59" <= ts <= "hgt:76":
            hgt = 1

    t = re.findall("hcl:#[0-9a-f]+[ |\n]", s)
    if len(t) == 1 and len(t[0]) == 12: # 6 + hcl: space or \n
        hcl = 1

    t = re.findall("ecl:(amb|blu|brn|gry|grn|hzl|oth)[ |\n]", s)
    if len(t) == 1:
        ecl = 1

    t = re.findall("pid:[0-9]+[ |\n]", s)
    if len(t) == 1 and len(t[0]) == 14: # 9 + pid: space or \n
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
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = f.readlines()

    print(numValid(inputs))

# 133 my answer
