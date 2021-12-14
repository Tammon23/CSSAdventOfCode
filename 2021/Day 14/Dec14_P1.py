from collections import Counter

file = "example_input.txt"
# file = "input.txt"


def SomeFunction(polymer_template, pair_insertions, num_steps):
    step = 1
    while step <= num_steps:
        i = 0
        while i < len(polymer_template) - 1:
            pair = polymer_template[i]+polymer_template[i+1]
            if pair in pair_insertions:
                polymer_template.insert(i+1, pair_insertions[pair])
                i+=2
            else:
                i+=1
        step+=1

    counts = Counter(polymer_template).values()
    return max(counts) - min(counts)


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        pt, pi = f.read().split("\n\n")
        pt = list(pt)
        npi = {}
        for r in pi.split("\n"):
            pair, insertion = r.split("->")
            npi[pair.strip()] = insertion.strip()

    print(SomeFunction(pt, npi, 10))
