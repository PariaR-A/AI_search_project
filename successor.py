import re

#getting the input
x , y = map(int, input().split())
matrix = []
#preparing the matrix
for i in range(x):
    value = list(input().split())
    matrix.append(value)
#our defualt energy
energy = 500


#our matrix value might be combination of letters and digits so we might need this to make it
def extract_digit_and_word(string):
    # Use regex to find the digit and word parts
    match = re.match(r"(\d+)(\w+)", string)
    
    if match:
        digit_part = match.group(1)
        word_part = match.group(2)
        return digit_part, word_part
    else:
        return None, None
    
#we should find our starting point to traverse
def find_starting_point(grid,energy):
    for row_idx, row in enumerate(grid):
        for col_idx, cell_value in enumerate(row):
            digit , word = extract_digit_and_word(cell_value)
            if (word == 'R'):
                energy -= int(digit)
                position = (row_idx, col_idx)
                return (position , energy)
            
                
            
    return None  # Return None if starting point not found




    
    
def successor(current_state, grid):
    successors = []
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Possible moves: right, left, down, up
    position = current_state[0]
    current_energy = current_state[1]
    current_row, current_col= position

    for move in moves:
        new_row = current_row + move[0]
        new_col = current_col + move[1]
        
        # Check if the new position is within the grid boundaries
        if 0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]):
            new_position = (new_row, new_col)
            cell_value = grid[new_row][new_col]
            if cell_value != 'X':  # 'X' represents an obstacl so no miving there
                new_energy = current_energy
                if cell_value.isdigit():  # Check if the cell value is a digit (cost)
                    cell_cost = int(cell_value)
                
                    if cell_cost <= current_energy:  # Check if the energy is sufficient to move to the new position
                        new_energy = current_energy - cell_cost
                        successors.append((new_position, new_energy))
                else:
                    reward = 0
                    digit , word = extract_digit_and_word(cell_value)
                    if word == 'C':  # Reward: C gives 10 energy
                        reward = 10
                    
                    elif word == 'B':  # Reward: B gives 5 energy
                        reward = 5
                    elif word == 'I':  # Reward: I gives 12 energy
                        reward = 12
                    elif word == 'T' or word == 'R':  # Target and start position, no energy change
                        reward =0
                    
                    cell_cost = int(digit) - reward
                    
                    if cell_cost <= current_energy:  # Check if the energy is sufficient to move to the new position
                        new_energy = current_energy - cell_cost
                        successors.append((new_position, new_energy))

    return successors

start = find_starting_point(matrix, energy)

print(successor(start, matrix))


#this comment exist for the sole purpose of git 
