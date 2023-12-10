from helper_functions import extract_digit_and_word
from Direction import Direction
from Node import Node

def successor(current_state, grid):
    """
    A function to get the children/successors of a current state given the grid
    """
    successors = []

    moves = []  # Possible moves: right, left, down, up
    for name, obj in Direction.__members__.items():
        moves.append(obj)

    position = current_state.position
    current_energy = current_state.remaining_energy
    current_row, current_col = position
    type = None

    for move_obj in moves:
        move = move_obj.value
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
                        successor_node.set_direction(move_obj.name)
                        successors.append(successor_node)
                else:
                    reward = 0
                    digit, word = extract_digit_and_word(cell_value)
                    if word == 'C':  # Reward: C gives 10 energy
                        reward = 10
                        type = None
                    elif word == 'B':  # Reward: B gives 5 energy
                        reward = 5
                        type = None
                    elif word == 'I':  # Reward: I gives 12 energy
                        reward = 12
                        type = None
                    elif word == 'T' :  # Target and start position, no energy change
                        reward = 0
                        type = 'T'
                    elif word == 'R':
                        reward =0
                        type = None

                    cell_cost = int(digit) - reward


                    if cell_cost <= current_energy:  # Check if the energy is sufficient to move to the new position
                        new_energy = current_energy - cell_cost
                        successor_node = Node(current_state, cell_cost, new_position, new_energy,type)
                        successor_node.set_direction(move_obj.name)
                        successors.append(successor_node)

    return successors


