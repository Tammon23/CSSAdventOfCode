from typing import Any, Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> str:
    return t.strip("\n")


def SomeFunction(data: Iterable[str]) -> Any:
    return data


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        # inputs = map(clean_input, f.readlines())
        inputs = f.readlines()

    print(SomeFunction(inputs))
