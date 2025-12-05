from typing import Any, Iterable

# file = "example_input.txt"
file = "input.txt"


def clean_input(t: str) -> Any:
    return list(t)


def solve(data: Iterable[str]) -> Any:
    data = list(data)
    dirs = [(0,1),(1,0),(0,-1),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
    ans = 0
    for r, row in enumerate(data):
        for c, val in enumerate(row):
            if val == "@":
                around = 0
                for dx, dy in dirs:
                    nx = r + dx
                    ny = c + dy
                    if 0 <= nx < len(data) and 0 <= ny < len(data[0]) and data[nx][ny] == "@":
                        around += 1
                if around < 4:
                    ans += 1
    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())
        # inputs = f.read().splitlines()

    print(solve(inputs))
