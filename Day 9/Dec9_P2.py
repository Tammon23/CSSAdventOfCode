def clean_input(t):
    return int(t.strip("\n"))


# from part 1
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


# finds the continuoous set that would make the invalid number
# then finds the encryption weakness
def find_encryption_weakness(data):
    c = []
    invalid = find_invalid(data)
    i = 0
    while 1:
        if len(c) == 0:
            c.append(data[i])
            i += 1
        elif sum(c) > invalid:
            c.pop(0)
            while sum(c) > invalid:
                c.pop(0)
        elif sum(c) < invalid:
            c.append(data[i])
            i += 1

        elif len(c) < 2:
            c.append(data[i])
            i += 1

        else:
            break

    return max(c) + min(c)


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(find_encryption_weakness(inputs))
