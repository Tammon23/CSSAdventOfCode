from z3 import Real, Solver, sat


file = "example_input.txt"
# file = "input.txt"


def solve() -> int | None:
    Position = [Real("px"), Real("py"), Real("pz")]
    Velocity = [Real("vx"), Real("vy"), Real("vz")]

    solver = Solver()

    for t in range(len(rocks)):
        time = Real(f'time_{t}')
        pos, vel = rocks[t]
        for axis in range(3):
            solver.add(Position[axis] + time * Velocity[axis] == pos[axis] + time * vel[axis])
    if solver.check() == sat:
        model = solver.model()
        return sum(model.evaluate(axis).as_long() for axis in Position)

    return None


if __name__ == "__main__":
    rocks = []

    # reading in the input
    with open(file, "r") as f:
        for i, line in enumerate(f.read().splitlines()):
            position, velocity = line.split(" @ ")
            rocks.append((tuple(map(int, position.split(", "))), tuple(map(int, velocity.split(", ")))))
    print(solve())
