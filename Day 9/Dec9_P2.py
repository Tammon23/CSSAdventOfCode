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


# finds the continuous set that would make the invalid number
# then finds the encryption weakness
def find_encryption_weakness(data):
    continuous_list = []
    invalid = find_invalid(data)
    i = 0
    while i < len(data):

        if len(continuous_list) < 2:
            continuous_list.append(data[i])
            i += 1
            continue

        continuous_list_sum = sum(continuous_list)
        if continuous_list_sum > invalid:
            continuous_list.pop(0)
            while sum(continuous_list) > invalid:
                continuous_list.pop(0)

        elif continuous_list_sum < invalid:
            continuous_list.append(data[i])
            i += 1

        else:
            break

    if i == len(data):
        return None
    return max(continuous_list) + min(continuous_list)


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(find_encryption_weakness(inputs))
