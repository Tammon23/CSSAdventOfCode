from collections import defaultdict

file = "example_input.txt"
# file = "input.txt"


def SomeFunction(data):
    monkeys = defaultdict(list)
    monkey_inspect = defaultdict(int)
    monkeys_data = {}
    t = data.split("\n\n")
    for line in t:
        monkey, starting_items, operation, test, truetest, falsetest = [t.strip() for t in line.split("\n")]
        monkey = int(monkey[7])
        starting_items = list(map(int, starting_items[16:].split(", ")))
        operation = operation[17:]
        truetest = int(truetest[-1])
        falsetest = int(falsetest[-1])
        test = int(test[19:])

        operation = lambda old, operation=operation: eval(operation)

        monkeys_data[monkey] = operation, test, truetest, falsetest
        monkeys[monkey] = starting_items + monkeys[monkey]

    nMonkeys = len(t)

    magic = 1
    for x in monkeys_data.values():
        magic *= x[1]

    for i in range(10000):
        for monkey in range(nMonkeys):
            operation, test, truetest, falsetest = monkeys_data[monkey]
            for item in monkeys[monkey]:
                monkey_inspect[monkey] += 1
                worry_level = operation(item) % magic
                if worry_level % test == 0:
                    monkeys[truetest] += [worry_level]
                else:
                    monkeys[falsetest] += [worry_level]

            monkeys[monkey] = []

    *_, a, b = sorted(list(monkey_inspect.values()))[-2:]
    return a * b


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = f.read()

    print(SomeFunction(inputs))
