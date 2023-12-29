file = "input.txt"


def clean_input(t: str) -> list[str]:
    return t.replace(" -> ", " ").split(" ")


def solve(goal: str) -> None:
    nxt = identifiers[goal]

    if len(nxt) == 1:  # x -> y or x -> 'int'
        if nxt[0].isnumeric():
            result = int(nxt[0])
        else:
            solve(nxt[0])
            result = seen[nxt[0]]

    elif len(nxt) == 2:  # NOT
        _, value = nxt
        if value not in seen:
            solve(value)

        result = ~seen[value] & 0xffff

    elif nxt[1] == "AND":
        left, _, right = nxt

        if left.isnumeric():
            left = int(left)
        else:
            if left not in seen:
                solve(left)
            left = seen[left]

        if right.isnumeric():
            right = int(right)
        else:
            if right not in seen:
                solve(right)
            right = seen[right]

        result = left & right

    elif nxt[1] == "OR":
        left, _, right = nxt

        if left.isnumeric():
            left = int(left)
        else:
            if left not in seen:
                solve(left)
            left = seen[left]

        if right.isnumeric():
            right = int(right)
        else:
            if right not in seen:
                solve(right)
            right = seen[right]

        result = left | right

    elif nxt[1] == "LSHIFT":
        left, _, shift = nxt
        if left not in seen:
            solve(left)

        result = seen[left] << int(shift)

    else:  # RSHIFT
        left, _, shift = nxt
        if left not in seen:
            solve(left)

        result = seen[left] >> int(shift)

    seen[goal] = result
    return


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    identifiers = {}
    for line in inputs:
        *operation, res = line
        identifiers[res] = operation

    seen = {}
    solve("a")
    identifiers["b"] = [str(seen["a"])]
    seen.clear()
    solve("a")
    print(seen["a"])
