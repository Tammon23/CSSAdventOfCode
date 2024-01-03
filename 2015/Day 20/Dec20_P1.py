file = "input.txt"


def solve(target_presents: int) -> int:
    target_presents //= 10
    sieve = [0] * target_presents
    for elf in range(1, target_presents):
        for house in range(elf, target_presents, elf):
            sieve[house] += elf * 10

    target_presents *= 10

    for i, num in enumerate(sieve):
        if num >= target_presents:
            return i

    return -1


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = int(f.read().strip())

    print(solve(inputs))
