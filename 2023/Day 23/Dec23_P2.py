from math import inf

import Helper

file = "example_input.txt"
# file = "input.txt"


dfs_seen = set()


def dfs(start_r: int, start_c: int) -> int:
    if start_r == len(inputs) - 1 and start_c == len(inputs[0]) - 2:
        return 0

    best_length = -inf
    dfs_seen.add((start_r, start_c))
    for next_r, next_c in graph[start_r, start_c]:
        if (next_r, next_c) not in dfs_seen:
            best_length = max(best_length, dfs(next_r, next_c) + graph[start_r, start_c][next_r, next_c])
    dfs_seen.remove((start_r, start_c))

    return best_length


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = [[v if v not in "><^v" else "." for v in x] for x in f.read().splitlines()]

    nbr_count = [(0, 1), (len(inputs) - 1, len(inputs[0]) - 2)]

    for r, row in enumerate(inputs):
        for c, val in enumerate(row):
            nbr = 0
            for dr, dc in Helper.strs_to_directions.values():
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(inputs) and 0 <= nc < len(inputs[0]) and inputs[nr][nc] != "#":
                    nbr += 1

            if inputs[r][c] != "#" and nbr > 2:
                nbr_count.append((r, c))

    graph = {nbr: {} for nbr in nbr_count}

    for sr, sc in nbr_count:
        stack = [(sr, sc, 0)]
        seen = {(sr, sc)}

        while stack:
            r, c, length = stack.pop()
            if length != 0 and (r, c) in nbr_count:
                graph[sr, sc][r, c] = length
                continue

            for dr, dc, in Helper.strs_to_directions.values():
                nr = r + dr
                nc = c + dc
                if 0 <= nr < len(inputs) and 0 <= nc < len(inputs[0]) and inputs[nr][nc] == "." and (nr, nc) not in seen:
                    stack.append((nr, nc, length + 1))
                    seen.add((nr, nc))

    print(dfs(0, 1))
