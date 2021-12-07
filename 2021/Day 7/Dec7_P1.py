from statistics import median

file = "example_input.txt"
# file = "input.txt"

def SomeFunction(data):
    num = int(median(data))
    return sum([abs(crab - num) for crab in data])


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(int, f.read().strip().split(",")))

    print(SomeFunction(inputs))