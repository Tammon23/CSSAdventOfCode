# file = "example_input.txt"
file = "input.txt"


def clean_input(t):
    _in, _out = t.strip("\n").split("|")
    return _in.strip().split(" "), _out.strip().split(" ")


def find_digits(_in):
    digits = {}  # number of segments : list of choice with said number of segments
    re = {}  # map of the known number to combination of symbols
    for digit in _in:
        d = len(digit)
        if d == 2:
            re[1] = frozenset(digit)
        elif d == 3:
            re[7] = frozenset(digit)
        elif d == 4:
            re[4] = frozenset(digit)
        elif d == 7:
            re[8] = frozenset(digit)
        else:
            digits[d] = digits.get(d, []) + [frozenset(digit)]

    # Setting 3
    for option in digits[5]:
        if len(option - re[1]) == (len(option) - 2):
            re[3] = option
            digits[5].remove(option)
            break

    # setting 2 & 5
    option1, option2 = digits[5]
    if len(option1 - re[4]) == 2:
        re[5] = option1
        re[2] = option2
    else:
        re[2] = option1
        re[5] = option2

    # setting 6
    for option in digits[6]:
        if len(option - re[1]) == (len(option) - 1):
            re[6] = option
            digits[6].remove(option)
            break

    # setting 0 & 9
    option1, option2 = digits[6]
    if len(option1 - re[4]) == 2:
        re[9] = option1
        re[0] = option2
    else:
        re[0] = option1
        re[9] = option2

    # returning the inverse of the dict, keys become values, values become keys
    return {re[key]: key for key in re}


def SomeFunction(data):
    total = 0
    for line in data:
        _in, _out = line
        sub_total = 0
        decoder = find_digits(_in)
        for i, c in enumerate(reversed(_out)):
            sub_total += decoder[frozenset(c)] * (10 ** i)
        total += sub_total

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
