from collections import defaultdict
from typing import List

file = "example_input.txt"
# file = "input.txt"


def solve(data: List[str]) -> int:
    total = 0
    # boxes > label > lens
    boxes = defaultdict(dict)

    for step in data:
        box = 0
        if "=" in step:
            label, lens = step.split("=")
            for ch in label:
                box += ord(ch)
                box *= 17
                box %= 256

            boxes[box][label] = int(lens)

        else:
            label = step[:-1]
            for ch in label:
                box += ord(ch)
                box *= 17
                box %= 256

            if label in boxes[box]:
                boxes[box].pop(label)

        total = 0
        for box in boxes:
            for i, label in enumerate(boxes[box], 1):
                total += (box + 1) * i * boxes[box][label]

    return total


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        initialization_sequence = f.read().strip("\n").split(",")
    print(solve(initialization_sequence))
