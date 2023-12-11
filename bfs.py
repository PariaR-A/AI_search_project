from successor import successor
from copy import deepcopy
from collections import deque  # Import deque for using a queue

def bfs(matrix, start, targetN):
    visited = set()  # Set to track visited nodes
    visited_nodes = []
    queue = deque([start])  # Use deque as a queue
    print(queue)
    print(targetN)
    target_num = deepcopy(targetN)

    while queue and target_num > 0:
        current_node = queue.popleft()  # Dequeue the leftmost node
        if current_node not in visited:
            visited_nodes.append(current_node)
        visited.add(current_node)

        # Check if the current node is one of the target points
        if current_node.type == 'T':
            target_num -= 1

        # Get successors of the current node
        successors = successor(current_node, matrix)

        # Add unvisited successors to the queue
        unvisited_successors = [succ for succ in successors if succ not in visited]
        queue.extend(unvisited_successors)

    # Reconstruct and print the path
    print("-------- Path --------")
    for node in visited_nodes:
        print(f"Node: {node.position}, Parent: {node.parent.position if node.parent else None}")
    print("-------- End Path --------")

    print("---- Remained Energy: ", visited_nodes[-1].remaining_energy)