# o(n^2) solution

# removes the from the input then returns the
# int value of it
def clean_input(t):
    return int(t.strip("\n"))


# given a list finds 3 numbers
# which add up to 2020
def find_numbers(numbers):
    hashed_numbers = set(numbers)

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if 2020 - numbers[i] - numbers[j] in hashed_numbers:
                return (2020 - numbers[i] - numbers[j]) * numbers[j] * numbers[i]


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = list(map(clean_input, f.readlines()))

    print(find_numbers(inputs))
