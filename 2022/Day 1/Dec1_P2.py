# file = "example_input.txt"
file = "input.txt"


# easy answer
def SomeFunction(data):
    cals = []
    temp = 0
    for line in data:
        if line == "\n":
            cals.append(temp)
            temp = 0
        else:
            temp += int(line.strip())
    cals.sort()
    return sum(cals[-3:])


# better memory usage
def SomeFunction2(data):
    res = [float('-inf')] * 3
    temp = 0
    for line in data:
        if line == "\n":
            for i, v in enumerate(res):
                if v < temp:
                    res[i] = temp
                    temp = v
            temp = 0
        else:
            temp += int(line.strip())
    return sum(res)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.readlines()

    print(SomeFunction(inputs))
    print(SomeFunction2(inputs))
