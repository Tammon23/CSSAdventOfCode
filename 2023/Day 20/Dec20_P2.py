from collections import deque, defaultdict
from math import lcm

file = "input.txt"


def press_button(press_button_calls: int, feed: str) -> None | int:
    global module_types, module_bit, broadcaster, path, conjunctions_mappings, seen, cycle_lengths
    q = deque(broadcaster)

    while q:
        cur, high_signal_strength, prev = q.popleft()
        if cur == feed and high_signal_strength:
            seen[prev] = True

            if prev not in cycle_lengths:
                cycle_lengths[prev] = press_button_calls
            else:
                assert press_button_calls == seen[prev] * cycle_lengths[prev]

            if all(seen.values()):
                return lcm(*cycle_lengths.values())

        if cur in module_types:
            if module_types[cur] == "%":
                if high_signal_strength:
                    continue
                else:
                    module_bit[cur] = not module_bit[cur]
                    for nxt in path[cur]:
                        q.append((nxt, module_bit[cur], cur))
            else:
                conjunctions_mappings[cur][prev] = high_signal_strength
                next_pulse = not all(conjunctions_mappings[cur].values())

                for nxt in path[cur]:
                    q.append((nxt, next_pulse, cur))

    return None


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

    module_bit["rx"] = False
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

    (rx_direct_paths, ) = [source for source, dest in path.items() if "rx" in dest]
    cycle_lengths = {}
    seen = {source: False for source, dest in path.items() if rx_direct_paths in dest}

    button_presses = 0
    while True:
        button_presses += 1
        res = press_button(button_presses, rx_direct_paths)
        if res is not None:
            print(res)
            break
