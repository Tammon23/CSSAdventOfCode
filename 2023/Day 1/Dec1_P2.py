from typing import List, Iterable

# file = "example_input2.txt"
file = "input.txt"


def clean_input(t: str) -> str:
    return t.strip("\n")


def solve(data: Iterable[str]) -> int:
    english_numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    english_numbers_reversed = [num[::-1] for num in english_numbers]

    return sum(int(get_digit(line, english_numbers) + get_digit(line[::-1], english_numbers_reversed))
               for line in data)


def get_digit(line: str, english_numbers: List[str]) -> str:
    for i, c in enumerate(line):
        if c.isdigit():
            return c
        for j, word in enumerate(english_numbers):
            if line[i:].startswith(word):
                return str(j + 1)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.readlines())

    print(solve(inputs))
