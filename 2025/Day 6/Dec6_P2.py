import re

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> list[int]:
    return "".join(t).strip()


def solve(data: list[str], operators: list[str]) -> int:
    total = 0
    operator_index = 0
    temp = operators[operator_index] != "+"

    for number in data:
        if number == "":
            total += temp
            operator_index += 1
            temp = operators[operator_index] != "+"

        else:
            x = int(number)
            if operators[operator_index] == "+":
                temp += x
            else:
                temp *= x

    return total + temp


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        *numbers, operators = f.read().splitlines()
    longest = max(len(number) for number in numbers)
    numbers = map(clean_input, [list(row) for row in zip(*map(lambda x: x.ljust(longest), numbers))])
    operators = re.findall(r"[*+]", operators)

    print(solve(numbers, operators))
