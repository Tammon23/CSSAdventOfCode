from statistics import mean

file = "example_input.txt"
# file = "input.txt"


def SomeFunction(data):
    # n(n+1)/2 equation of series, optimal number somewhere in the middle
    # test all cases
    num = round(mean(data))
    c1 = sum([(abs(crab - num) * (abs(crab - num) + 1)) for crab in data])
    c2 = sum([(abs(crab - num-1) * (abs(crab - num-1) + 1)) for crab in data])
    c3 = sum([(abs(crab - num+1) * (abs(crab - num+1) + 1)) for crab in data])
    return int(min(c1, c2, c3)/2)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(int, f.read().strip().split(",")))

    print(SomeFunction(inputs))