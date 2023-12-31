from functools import reduce
from typing import Tuple, Iterable, Any, Self


class Directions:
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


strs_to_directions = {
    "U": Directions.UP,
    "D": Directions.DOWN,
    "L": Directions.LEFT,
    "R": Directions.RIGHT
}


# thank you https://stackoverflow.com/a/287944/19236048
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class Vector:
    def __init__(self, description: str, *args):
        self.description = description
        self.vec = {label: value for label, value in zip(description.split(" "), args)}

        for name, value in self.vec.items():
            setattr(self, name, value)

    def get_as_tuple(self) -> Tuple[Any, ...]:
        return tuple(value for value in self.vec.values())

    def __repr__(self):
        return f"Vector {{{" ".join(f"{name}={value}" for name, value in self.vec.items())}}}"

    def __add__(self, other: int | Self):
        vec = self.vec
        if isinstance(other, int):
            return Vector(self.description, *(vec[label] + other for label in vec))

        return Vector(self.description, *(vec[label] + other.vec[label] for label in vec))

    def __mul__(self, other: int | Self):
        vec = self.vec
        if isinstance(other, int):
            return Vector(self.description, *(vec[label] * other for label in vec))

        return Vector(self.description, *(vec[label] * other.vec[label] for label in vec))

    def __sub__(self, other: int | Self):
        vec = self.vec
        if isinstance(other, int):
            return Vector(self.description, *(vec[label] - other for label in vec))

        return Vector(self.description, *(vec[label] - other.vec[label] for label in vec))

    def __isub__(self, other: int | Self):
        vec = self.vec
        if isinstance(other, int):
            return Vector(self.description, *(other - vec[label] for label in vec))

        return Vector(self.description, *(other.vec[label] - vec[label] for label in vec))

    def __floordiv__(self, other: int | Self):
        vec = self.vec
        if isinstance(other, int):
            return Vector(self.description, *(vec[label] // other for label in vec))

        return Vector(self.description, *(vec[label] // other.vec[label] for label in vec))

    def __ifloordiv__(self, other):
        vec = self.vec
        if isinstance(other, int):
            return Vector(self.description, *(other // vec[label] for label in vec))

        return Vector(self.description, *(other.vec[label] // vec[label]for label in vec))

    def __truediv__(self, other: int | Self):
        vec = self.vec
        if isinstance(other, int):
            return Vector(self.description, *(vec[label] / other for label in vec))

        return Vector(self.description, *(vec[label] / other.vec[label] for label in vec))

    def __itruediv__(self, other):
        vec = self.vec
        if isinstance(other, int):
            return Vector(self.description, *(other / vec[label] for label in vec))

        return Vector(self.description, *(other.vec[label] / vec[label] for label in vec))


def product(values: Iterable[int]):
    return reduce(lambda x, y: x * y, values)


def colourize(text: str, colour: bcolors = bcolors.FAIL) -> str:
    return f"{colour}{text}\033[0m"


def get_min_max_at_index(iterable: Iterable[Tuple[int, int]], index: int) -> Tuple[int, int]:
    return min(value[index] for value in iterable), max(value[index] for value in iterable)


def rotate_point_90cw(point: Tuple[int, int]) -> Tuple[int, int]:
    return point[1], -point[0]


def rotate_point_180cw(point: Tuple[int, int]) -> Tuple[int, int]:
    return -point[0], -point[1]


def rotate_point_90ccw(point: Tuple[int, int]) -> Tuple[int, int]:
    return -point[1], point[0]


def pprint_array(array: Iterable[Iterable[Any]], join_row=True, join_sep="") -> None:
    for row in array:
        if join_row:
            print(join_sep.join(row))
        else:
            print(row)


def add_tuple(tuple1: [Tuple[int, int]], tuple2: [Tuple[int, int]]) -> Tuple[int, int]:
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def subtract_tuple(tuple1: [Tuple[int, int]], tuple2: [Tuple[int, int]]) -> Tuple[int, int]:
    return tuple1[0] - tuple2[0], tuple1[1] - tuple2[1]


def multiply_tuple(tuple1: [Tuple[int, int]], scaler: int | float) -> Tuple[int, int] | Tuple[float, float]:
    return tuple1[0] * scaler, tuple1[1] * scaler
