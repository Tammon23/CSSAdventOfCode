from typing import Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> tuple[str, int, int, int]:
    reindeer, _, _, speed, _, _, move_time, *_, rest_time, _ = t.split(" ")
    return reindeer, int(speed), int(move_time), int(rest_time)


def solve(reindeer_stats: Iterable[tuple[str, int, int, int]], elapsed_time: int) -> int:
    ans = -1
    for horse, speed, move_time, rest_time in reindeer_stats:
        div, mod = divmod(elapsed_time, move_time + rest_time)
        cur = div * speed * move_time + speed * min(move_time, mod)
        ans = max(cur, ans)
    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    # example elapsed_time is 1000s, answer should be 2503s
    print(solve(inputs, 1000))
