from successor import successor
from copy import deepcopy
from Direction import get_directions_dict


def dfs(matrix, start, targetN):
    visited = set()  # Set to track visited nodes
    visited_nodes = []
    stack = [start]  # Stack to hold nodes to be processed
    print(stack)
    print(targetN)
    target_num = deepcopy(targetN)

    while stack and target_num > 0:
        current_node = stack.pop()
        if current_node not in visited:
            visited_nodes.append(current_node)
        visited.add(current_node)

        # Check if the current node is one of the target points
        if current_node.type == 'T':
            target_num -= 1

        # Get successors of the current node
        successors = successor(current_node, matrix)

        # Add unvisited successors to the stack
        unvisited_successors = [succ for succ in successors if succ not in visited]
        stack.extend(unvisited_successors)

    # Reconstruct and print the path
    print("-------- Path --------")

    direction_dict = get_directions_dict()

    for node in visited_nodes:
        if node.direction != None:
            direction_name_abv = direction_dict[node.direction]
            print(f"{direction_name_abv}", end=", ")
    print("")
    print("-------- End Path --------")

    print("---- Remained Energy: ", visited_nodes[-1].remaining_energy)