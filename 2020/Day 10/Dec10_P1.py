# given a list of adapters finds the number
# of jolt differences in the data
# then multipliers the 1-jolts by the 3-jolts
def find_jolt_differences(data):
    difference = [0, 0, 1]
    difference[data[0]-1] += 1
    i = 1

    # looping through each element in data
    # and recording the differences in an array
    while i < len(data):
        diff = data[i] - data[i - 1]
        difference[diff - 1] += 1
        i += 1
    return difference[0] * difference[2]


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = sorted(list(map(int, f.read().split("\n"))))

    print(find_jolt_differences(inputs))
