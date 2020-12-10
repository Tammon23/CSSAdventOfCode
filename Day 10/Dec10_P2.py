# finds the total number of distinct ways you can arrange
# the adapters to connect the charging outlet to your device
def find_num_adaptor_combinations(i, data, mem):
    # memoization for performance
    if i in mem:
        return mem[i]

    numBranches = 0
    # looping through each element and seeing if we can create a
    # new branch from it opposed to doing x in data to improve perfomance
    for index in range(i, len(data)):
        if data[i] + 1 == data[index]:
            numBranches += find_num_adaptor_combinations(index, data, mem)
        if data[i] + 2 == data[index]:
            numBranches += find_num_adaptor_combinations(index, data, mem)
        if data[i] + 3 == data[index]:
            numBranches += find_num_adaptor_combinations(index, data, mem)
        if data[i] + 3 < data[index]:
            break

    # saving the number of child branches of a particular branch so we don't
    # need to recalculate it later
    mem[i] = 1 + numBranches if i == len(data) - 1 else numBranches
    return mem[i]


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(int, f.read().split('\n')))
        inputs.extend([0, max(inputs) + 3])
    print(find_num_adaptor_combinations(0, sorted(inputs), {}))
