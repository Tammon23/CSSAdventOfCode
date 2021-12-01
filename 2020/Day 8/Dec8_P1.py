def clean_input(t):
    t = t.strip("\n").split(" ")
    t[1] = int(t[1])
    return t[0], t[1]


# finds the accumulation value be a set of instructions
# before a loop occurs
def FindAccumulatorBeforeLoopBack(data):
    i = acc = 0
    visited = set()
    while 1:
        if i in visited:
            break

        visited.add(i)
        if data[i][0] == 'acc':
            acc += data[i][1]

        elif data[i][0] == 'jmp':
            i += data[i][1]
            continue

        i += 1

    return acc


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(FindAccumulatorBeforeLoopBack(inputs))
