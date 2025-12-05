from typing import Any, Iterable

file = "example_input.txt"
# file = "input.txt"

def clean_input(t: str) -> Any:
    return list(map(int, t.split("-")))

def solve(fresh: list[list[int]]) -> Any:
    fresh.sort()
    merged = [fresh[0]]
    for i in range(1, len(fresh)):
        start, end = fresh[i]
        if merged[-1][1] < start - 1:
            merged.append([start, end])
        else:
            merged[-1][1] = max(merged[-1][1], end)
    return sum(end - start + 1 for start, end in merged)



if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read().split("\n\n")
        fresh = list(map(clean_input, inputs[0].splitlines()))

    print(solve(fresh))
