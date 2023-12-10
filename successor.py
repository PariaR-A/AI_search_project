import re
from enum import Enum

class Direction(Enum):
    """
    Direction Enum for Top, Down, Left and Right.
    """
    Up = (-1, 0)
    Down = (1, 0)
    Left = (0, -1)
    Right = (0, 1)

class Node:
    def __init__(self, parents, cell_cost, position, remaining_energy,type):
        self.parents = parents
        self.cell_cost = cell_cost
        self.position = position
        self.remaining_energy = remaining_energy
        self.direction = None # Not set yet
        self.type = type
    
    def set_direction(self, direction: Direction):
        self.direction = direction


def get_input():
    """
    Function to get the input from the user
    """

    targetN =0
    x, y = map(int, input().split())
    input_matrix = []
    # preparing the matrix
    for i in range(x):
        value = list(input().split())
        for i in value:
            if 'T' in i:
                targenN +=1
        input_matrix.append(value)
    # our default energy
    energy = 500
    return input_matrix, energy ,targetN


def extract_digit_and_word(string):
    """
    our matrix value might be combination of letters and digits so we might need this to parse it
    """
    match = re.match(r"(\d+)(\w+)", string)

    if match:
        digit_part = match.group(1)
        word_part = match.group(2)
        return digit_part, word_part
    else:
        return None, None


def find_starting_point(grid, energy):
    """
    find our starting point to traverse
    """
    for row_idx, row in enumerate(grid):
        for col_idx, cell_value in enumerate(row):
            digit, word = extract_digit_and_word(cell_value)
            if word == 'R':
                energy -= int(digit)
                position = (row_idx, col_idx)
                return Node([], 0, position, energy,'R')

    return None  # Return None if starting point not found


def successor(current_state, grid):
    """
    A function to get the children/successors of a current state given the grid
    """
    successors = []

    moves = []  # Possible moves: right, left, down, up
    for name, obj in Direction.__members__.items():
        moves.append(obj.value)

    position = current_state.position
    current_energy = current_state.remaining_energy
    current_row, current_col = position
    type = None

    for move in moves:
        new_row = current_row + move[0]
        new_col = current_col + move[1]

        # Check if the new position is within the grid boundaries
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            new_position = (new_row, new_col)
            cell_value = grid[new_row][new_col]
            if cell_value != 'X':  # 'X' represents an obstacle, so no moving there
                new_energy = current_energy
                if cell_value.isdigit():  # Check if the cell value is a digit (cost)
                    cell_cost = int(cell_value)

                    if cell_cost <= current_energy:  # Check if the energy is sufficient to move to the new position
                        new_energy = current_energy - cell_cost
                        successor_node = Node(current_state, cell_cost, new_position, new_energy,type)
                        successors.append(successor_node)
                else:
                    reward = 0
                    digit, word = extract_digit_and_word(cell_value)
                    if word == 'C':  # Reward: C gives 10 energy
                        reward = 10
                    elif word == 'B':  # Reward: B gives 5 energy
                        reward = 5
                    elif word == 'I':  # Reward: I gives 12 energy
                        reward = 12
                    elif word == 'T' :  # Target and start position, no energy change
                        reward = 0
                        type = 'T'
                    elif word == 'R':
                        reward =0

                    cell_cost = int(digit) - reward

                    if cell_cost <= current_energy:  # Check if the energy is sufficient to move to the new position
                        new_energy = current_energy - cell_cost
                        successor_node = Node(current_state, cell_cost, new_position, new_energy,type)
                        successors.append(successor_node)

    return successors
