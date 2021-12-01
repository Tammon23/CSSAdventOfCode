# file = "example_input.txt"
file = "input.txt"


def clean_input(t):
    return int(t.strip("\n"))


def SomeFunction(data):
    n = 0
    for i in range(len(data)-3):
        if sum(data[i:i+3]) < sum(data[i+1:i+1+3]):
            n += 1
    return n


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
