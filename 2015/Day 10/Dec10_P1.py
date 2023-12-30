file = "example_input.txt"
# file = "input.txt"


def solve(data: str) -> int:
    cur = list(data)
    for _ in range(40):
        cnt = 1
        nxt = []
        i = 0
        while i < len(cur) - 1:
            if cur[i] == cur[i + 1]:
                cnt += 1
            else:
                nxt.append(str(cnt))
                nxt.append(cur[i])
                cnt = 1

            i += 1

        nxt.append(str(cnt))
        nxt.append(cur[-1])

        cur = nxt

    return len(nxt)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().strip()

    print(solve(inputs))
