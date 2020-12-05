# o(n) solution

# removes the from the input then returns the
# int value of it
def clean_input(t):
    return int(t.strip("\n"))


# given a list finds 2 numbers
# which add up to 2020
def find_numbers(numbers):
    seen = set([0])
    for value in numbers:
        if 2020 - value in seen:
            return (2020 - value) * value
        else:
            seen.add(value)


if __name__ == "__main__":
    # reading in the input
    with open("input.txt", "r") as f:
        inputs = map(clean_input, f.readlines())
    print(find_numbers(inputs))
