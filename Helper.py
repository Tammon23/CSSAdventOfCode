from typing import Tuple, Iterable, Any


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


def get_min_max_at_index(iterable: Iterable[Tuple[int, int]], index: int) -> Tuple[int, int]:
    return min(value[index] for value in iterable), max(value[index] for value in iterable)


def rotate_point_90cw(point: Tuple[int, int]) -> Tuple[int, int]:
    return point[1], -point[0]


def rotate_point_180cw(point: Tuple[int, int]) -> Tuple[int, int]:
    return -point[0], -point[1]


def rotate_point_90ccw(point: Tuple[int, int]) -> Tuple[int, int]:
    return -point[1], point[0]


def pprint_array(array: Iterable[Iterable[Any]]) -> None:
    for row in array:
        print(row)


def add_tuple(tuple1: [Tuple[int, int]], tuple2: [Tuple[int, int]]) -> Tuple[int, int]:
    return tuple1[0] + tuple2[0], tuple1[1] + tuple2[1]


def subtract_tuple(tuple1: [Tuple[int, int]], tuple2: [Tuple[int, int]]) -> Tuple[int, int]:
    return tuple1[0] - tuple2[0], tuple1[1] - tuple2[1]


def multiply_tuple(tuple1: [Tuple[int, int]], scaler: int | float) -> Tuple[int, int] | Tuple[float, float]:
    return tuple1[0] * scaler, tuple1[1] * scaler
