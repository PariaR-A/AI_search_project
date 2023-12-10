from Direction import Direction
from helper_functions import print_colorful_text
from helper_functions import Color

class Node:
    def __init__(self, parent, cell_cost, position, remaining_energy,type):
        self.parent = parent
        self.cell_cost = cell_cost
        self.position = position
        self.remaining_energy = remaining_energy
        self.direction = None # Not set yet
        self.type = type
    
    def set_direction(self, direction: Direction):
        self.direction = direction

    def __repr__(self):
        if self.parent != None:
            return f'{print_colorful_text("<Node", Color.GREEN)} parent: {self.parent.position} - direction: {self.direction} - type: {self.type} - position: {self.position}{print_colorful_text(">", Color.GREEN)}'
        else:
            return f'{print_colorful_text("<Node", Color.GREEN)} parent: !NoParent! - direction: {self.direction} - type: {self.type} - position: {self.position}{print_colorful_text(">", Color.GREEN)}'
        

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.position == other.position
        return False

    def __hash__(self):
        return hash(self.position)
    