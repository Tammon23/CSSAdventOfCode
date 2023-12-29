from collections import defaultdict

file = "example_input.txt"
# file = "input.txt"


seen = set()


def solve(current: str, total: int = 0) -> int | float:
    if len(seen) == len(routes.keys()) - 1:
        return total

    seen.add(current)

    longest = -1

    for nxt in routes[current]:
        if nxt in seen:
            continue
        longest = max(solve(nxt, total + routes[current][nxt]), longest)

    seen.remove(current)
    return longest


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().splitlines()

    routes = defaultdict(dict)
    for line in inputs:
        to, from_, dst = line.replace(" = ", " ").replace(" to ", " ").split(" ")
        routes[to][from_] = int(dst)
        routes[from_][to] = int(dst)

    print(max(solve(r) for r in routes.keys()))
