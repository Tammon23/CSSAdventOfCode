def clean_input(t):
    return int(t.strip("\n"))


# finds the invalid number that causes
# the encoding error
def find_invalid(data):
    preamble = data[:25]
    data = data[25:]

    for element in data:
        options = sorted(preamble)
        i = 0
        j = 24
        solution = False

        while i < j:
            if options[i] + options[j] < element:
                i += 1
            elif options[i] + options[j] > element:
                j -= 1
            else:
                solution = True
                break

        if solution:
            preamble.pop(0)
            preamble.append(element)

        else:
            return element

    return None


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(find_invalid(inputs))
