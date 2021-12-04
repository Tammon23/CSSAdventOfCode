file = "example_input.txt"
# file = "input.txt"


def clean_input(t):
    return t.strip("\n")

# bad solution
def SomeFunction(data):
    bitsize = len(data[0])
    gamma = epsilon = ""
    zeros = bitsize * [0]
    ones = bitsize * [0]

    for string in data:
        for index, char in enumerate(string):
            if char == "0":
                zeros[index] += 1
            else:
                ones[index] += 1

    for i in range(bitsize):
        if zeros[i] > ones[i]:
            gamma += "0"
            epsilon += "1"
        else:
            gamma += "1"
            epsilon += "0"
    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.readlines()))
        # inputs = f.readlines()

    print(SomeFunction(inputs))
