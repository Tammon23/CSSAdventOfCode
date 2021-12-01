
def clean_input(t):
    return int(t.strip("\n"))


def SomeFunction(data):
    num = 0
    for i in range(len(data)-1):
        if data[i] < data[i+1]:
            num += 1
    return num


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(SomeFunction(inputs))
