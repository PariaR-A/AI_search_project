from Direction import Direction
from Node import Node
from helper_functions import extract_digit_and_word
from successor import successor

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
                targetN +=1
        input_matrix.append(value)
    # our default energy
    energy = 500
    return input_matrix, energy ,targetN


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
                return Node(None, 0, position, energy,'R')

    return None  # Return None if starting point not found


if __name__ == "__main__":
    matrix, const_energy, target_n = get_input()
    start = find_starting_point(matrix, const_energy)
    successors = successor(start, matrix)
    for s in successors:
        print("Parents:", s.parents.position if s.parents else "None")
        print("Cell Cost:", s.cell_cost)
        print("Position:", s.position)
        print("Remaining Energy:", s.remaining_energy)
        print()
