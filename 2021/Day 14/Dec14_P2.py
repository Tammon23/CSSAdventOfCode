from collections import Counter, defaultdict

file = "example_input.txt"
# file = "input.txt"


def SomeFunction(polymer_template, pair_insertions, num_steps):
    step = 1
    unfiltered_pairs = Counter((''.join(polymer_template[i:i+2])) for i in range(len(polymer_template)-1))

    while step <= num_steps:
        filtered_pairs = defaultdict(int)

        for pair, frequency in unfiltered_pairs.items():
            pair = ''.join(pair)
            if pair in pair_insertions:
                left_polymer, middle_polymer, right_polymer = pair[0], pair_insertions[pair], pair[1]

                # for each 2 new polymer pairs we find, we record that we found the
                # polymer pair and denote how many pairs it will create
                # since that pair may already exist, we increment instead of set
                filtered_pairs[left_polymer, middle_polymer] += frequency
                filtered_pairs[middle_polymer, right_polymer] += frequency

            else:
                # otherwise we just record this pair in our new pairs list
                filtered_pairs[pair] = frequency
        unfiltered_pairs = filtered_pairs.copy()
        step+=1

    # since we have a dict of pairs and their frequencies (NNCB -> {NN:1, NC:1, CB:1})
    # in order to count each letter's frequency once we focus on the
    # last character of each pair, and manually increment the first character
    # of the first pair
    counts = {}
    for key in unfiltered_pairs:
        counts[key[1]] = counts.get(key[1], 0) + unfiltered_pairs[key]
    counts[polymer_template[0]] + 1

    counts = counts.values()
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

    print(SomeFunction(pt, npi, 40))
