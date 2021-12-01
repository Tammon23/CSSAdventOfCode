if __name__=="__main__":
    print("Part 1:", sum(len(set(t.replace("\n", ""))) for t in "".join(open("input.txt").readlines()).split("\n\n")), "Part 2:", sum([(sum([1 if occurrence == group.count("\n") + 1 else 0 for _, occurrence in __import__('collections').Counter(group.replace("\n", "")).items()])) for group in "".join(open("input.txt").readlines()).split("\n\n")]))
