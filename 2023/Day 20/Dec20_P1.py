from collections import deque, defaultdict

file = "example_input.txt"
# file = "input.txt"

low = high = 0


def press_button() -> None:
    global low, high, module_types, module_bit, broadcaster, path, conjunctions_mappings
    q = deque(broadcaster)

    while q:
        cur, is_high, prev = q.popleft()
        if is_high:
            high += 1
        else:
            low += 1

        if cur in module_types:
            if module_types[cur] == "%":
                if is_high:
                    continue
                else:
                    module_bit[cur] = not module_bit[cur]
                    for nxt in path[cur]:
                        q.append((nxt, module_bit[cur], cur))
            else:
                conjunctions_mappings[cur][prev] = is_high
                next_pulse = not all(conjunctions_mappings[cur].values())

                for nxt in path[cur]:
                    q.append((nxt, next_pulse, cur))


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [x.split(" -> ") for x in f.read().splitlines()]

    broadcaster = None
    for r, row in enumerate(inputs):
        if row[0] == "broadcaster":
            _, broadcaster = inputs.pop(r)

    broadcaster = broadcaster.split(", ")
    path = {}
    module_types = {}
    module_bit = {}

    for row in inputs:
        flip = row[0][1:]
        module_types[flip] = row[0][0]
        module_bit[flip] = False
        path[flip] = row[1].split(", ")

    conjunctions = []
    for module, module_type in module_types.items():
        if module_type == "&":
            conjunctions.append(module)

    conjunctions_mappings = defaultdict(dict)

    for conjunction in conjunctions:
        for key, value in path.items():
            if conjunction in value:
                conjunctions_mappings[conjunction][key] = False

    broadcaster = [(x, False, "broadcaster") for x in broadcaster]

    button_presses = 1000
    for _ in range(button_presses):
        press_button()

    ans = (low + button_presses) * high
    print(ans)

