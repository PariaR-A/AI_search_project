from enum import Enum

class Direction(Enum):
    """
    Direction Enum for Top, Down, Left and Right.
    """
    Up = (-1, 0)
    Down = (1, 0)
    Left = (0, -1)
    Right = (0, 1)


def get_directions_dict():
    direction_dict = {"Up": "U", "Down": "D", "Left": "L", "Right": "R"}
    return direction_dict