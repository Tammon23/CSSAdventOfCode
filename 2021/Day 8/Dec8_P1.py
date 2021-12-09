file = "example_input.txt"


# file = "input.txt"


def clean_input(t):
    return t.strip("\n").split("|")[1].strip().split(" ")


def SomeFunction(data):
    result = {}
    for row in data:
        for digit in row:
            d = len(digit)
            if d == 2 or d == 3 or d == 4 or d == 7:
                result[d] = result.get(d, 0) + 1

    return sum([result[count] for count in result])


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
