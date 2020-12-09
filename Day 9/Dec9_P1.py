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
        j = 24  # capture size of preamble -1

        while i < j:
            testing_sum = options[i] + options[j]
            if testing_sum < element:
                i += 1
            elif testing_sum > element:
                j -= 1
            else:
                break

        if testing_sum != element:
            return element

        preamble.pop(0)
        preamble.append(element)

    return None


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(find_invalid(inputs))
