file = "example_input.txt"


# file = "input.txt"

def clean_input(t):
    return t.strip("\n")


def SomeFunction(oxylist, co2list, index=0):
    if len(oxylist) == 1 and len(co2list) == 1:
        return int(oxylist[0], 2) * int(co2list[0], 2)

    zeroes, ones = [], []

    if len(oxylist) > 1:
        for string in oxylist:
            if string[index] == "0":
                zeroes.append(string)

            else:
                ones.append(string)

        oxylist = zeroes.copy() if len(zeroes) > len(ones) else ones.copy()

    zeroes.clear()
    ones.clear()
    if len(co2list) > 1:
        for string in co2list:
            if string[index] == "0":
                zeroes.append(string)

            else:
                ones.append(string)

        co2list = zeroes.copy() if len(zeroes) <= len(ones) else ones.copy()

    return SomeFunction(oxylist, co2list, index + 1)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))
        # inputs = f.readlines()

    print(SomeFunction(inputs, inputs))