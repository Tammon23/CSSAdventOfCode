from typing import Any, Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> Any:
    return t


def solve(data: Iterable[str]) -> Any:
    not_allowed = {"ab", "cd", "pq", "xy"}
    ans = 0
    for string in data:
        vowel_counts = dict.fromkeys("aeiou", 0)
        found_double = False
        for i in range(len(string) - 1):
            cur = string[i]
            if cur in vowel_counts:
                vowel_counts[cur] += 1

            if string[i] == string[i + 1]:
                found_double = True

            if string[i:i+2] in not_allowed:
                break
        else:
            if string[-1] in vowel_counts:
                vowel_counts[string[-1]] += 1

            if found_double and sum(vowel_counts.values()) > 2:
                ans += 1

    return ans


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        # inputs = map(clean_input, f.read().splitlines())
        inputs = f.read().splitlines()

    print(solve(inputs))
