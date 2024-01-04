# file = "example_input.txt"
file = "input.txt"


def clean_input(t: str) -> list[str]:
    return t.replace(",", "").split(" ")


def solve(data: list[list[str]]) -> dict[str, int]:
    registers = {"a": 1, "b": 0}

    current_instruction = 0
    while current_instruction < len(data):
        instruction = data[current_instruction]

        match instruction[0]:
            case "hlf":
                _, register = instruction
                registers[register] //= 2

            case "tpl":
                _, register = instruction
                registers[register] *= 3

            case "inc":
                _, register = instruction
                registers[register] += 1

            case "jmp":
                _, offset = instruction
                current_instruction += int(offset) - 1

            case "jie":
                _, register, offset = instruction
                if registers[register] % 2 == 0:
                    current_instruction += int(offset) - 1

            case "jio":
                _, register, offset = instruction
                if registers[register] == 1:
                    current_instruction += int(offset) - 1

        current_instruction += 1

    return registers


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = list(map(clean_input, f.read().splitlines()))

    print(solve(inputs)["b"])
