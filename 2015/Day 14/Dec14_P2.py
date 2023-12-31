from typing import Iterable

file = "example_input.txt"
# file = "input.txt"


def clean_input(t: str) -> tuple[str, int, int, int]:
    reindeer, _, _, speed, _, _, move_time, *_, rest_time, _ = t.split(" ")
    return reindeer, int(speed), int(move_time), int(rest_time)


def solve(reindeer_stats: Iterable[tuple[str, int, int, int]], race_length: int) -> int:
    better_reindeer_stats = {}
    for reindeer, speed, move_time, rest_time in reindeer_stats:
        better_reindeer_stats[reindeer] = {
            "points": 0,
            "speed": speed,
            "moved": 0,
            "max_move_time": move_time,
            "rested": 0,
            "max_rest_time": rest_time,
            "position": 0
        }

    for _ in range(race_length):
        for deer in better_reindeer_stats:
            cur = better_reindeer_stats[deer]
            if cur["moved"] == cur["max_move_time"]:
                cur["rested"] += 1
                if cur["rested"] == cur["max_rest_time"]:
                    cur["rested"] = 0
                    cur["moved"] = 0

            else:
                cur["moved"] += 1
                cur["position"] += cur["speed"]

        best = -1
        best_names = []
        for deer in better_reindeer_stats:
            cur = better_reindeer_stats[deer]
            if cur["position"] > best:
                best = cur["position"]
                best_names = [deer]

            elif cur["position"] == best:
                best_names.append(deer)

        for deer in best_names:
            better_reindeer_stats[deer]["points"] += 1

    return max(x["points"] for x in better_reindeer_stats.values())


if __name__ == "__main__":
    # reading in the input
    with open(file, "r") as f:
        inputs = map(clean_input, f.read().splitlines())

    # example elapsed_time is 1000s, answer should be 2503s
    print(solve(inputs, 2503))
