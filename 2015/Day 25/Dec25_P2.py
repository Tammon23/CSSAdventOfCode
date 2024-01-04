file = "example_input.txt"
# file = "input.txt"


def solve(row: int, col: int) -> int:
    fill_order = col

    cur = 1
    for _ in range(row - 1 + col - 1):
        fill_order += cur
        cur += 1

    prev = 20151125
    for _ in range(fill_order - 1):
        prev *= 252533
        prev %= 33554393

    return prev


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().split(" ")

    r = int(inputs[-3][:-1])
    c = int(inputs[-1][:-1])

    print(solve(r, c))
