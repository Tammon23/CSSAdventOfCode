from typing import Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> tuple[str, tuple[int, ...], tuple[int, ...]]:
    r = t.split(" ")
    if len(r) == 5:
        _, state, start, _, end = r

    else:
        state, start, _, end = r

    start = tuple(map(int, start.split(",")))
    end = tuple(map(int, end.split(",")))

    return state, start, end


def solve(data: Iterable[tuple[str, tuple[int, ...], tuple[int, ...]]]) -> int:

    lit = set()
    for line in data:
        state, start, end = line

        for r in range(start[0], end[0] + 1):
            for c in range(start[1], end[1] + 1):
                if state == "off":
                    lit.discard((r, c))
                elif state == "on":
                    lit.add((r, c))
                else:
                    if (r, c) in lit:
                        lit.remove((r, c))
                    else:
                        lit.add((r, c))

    return len(lit)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    print(solve(inputs))
