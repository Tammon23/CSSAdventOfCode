from Dec9_P1 import find_invalid


def clean_input(t):
    return int(t.strip("\n"))


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
