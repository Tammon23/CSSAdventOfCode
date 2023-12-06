file = "example_input.txt"
# file = "input.txt"


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        lines = f.readlines()

    seeds = set(list(map(int, set(lines[0].split(":")[1].strip().split(" ")) - {''})))
    maps = [dict() for _ in range(7)]
    last_line = 3
    prev = seeds

    for i in range(7):
        for line in lines[last_line:]:
            if line == "\n":
                last_line += 2
                break
            dest_start, source_start, length = map(int, line.split(" "))
            for seed in prev:
                if source_start <= seed < source_start + length:
                    maps[i][seed] = (seed - source_start) + dest_start

            last_line += 1

        for key in prev:
            if key not in maps[i]:
                maps[i][key] = key

        prev = maps[i].values()

    print(min(maps[-1].values()))
