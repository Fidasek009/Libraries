import heapq

# stolen from: https://gist.github.com/ryancollingwood/32446307e976a11a1185a5394d6657bc

class Node():
    """A node class for A* Pathfinding"""

    def __init__(self, parent=None, position=None):
        self.parent: Node = parent
        self.position: tuple[int] = position

        self.g = 0  # G cost (distance from start)
        self.h = 0  # H cost (heuristic = estimated distance from end)
        self.f = 0  # H cost + G cost


    def __eq__(self, other):
        return self.position == other.position
    

    def __repr__(self):
      return f"{self.position} - g: {self.g} h: {self.h} f: {self.f}"


    # defining less than for purposes of heap queue
    def __lt__(self, other):
      return self.f < other.f
    

    # defining greater than for purposes of heap queue
    def __gt__(self, other):
      return self.f > other.f



class Maze:
    map: list[list[bool]] # to access by coordinates use (y, x)

    def __init__(self, mapList: list[list[bool]], diagonalMovement: bool=True) -> None:
        self.map = mapList
        self.allow_diagonal_movement = diagonalMovement


    def return_path(self, current_node: Node):
        path = []
        current = current_node
        while current is not None:
            path.append(current.position)
            current = current.parent
        return path[::-1]  # Return reversed path


    def astar(self, start: tuple[int], end: tuple[int]):
        # Create start and end node
        start_node = Node(None, start)
        end_node = Node(None, end)

        # Initialize both open and closed list
        open_list = []
        closed_list = []


        # Heapify the open_list and Add the start node
        heapq.heapify(open_list) 
        heapq.heappush(open_list, start_node)

        # Adding a stop condition
        outer_iterations = 0
        max_iterations = (len(self.map[0]) * len(self.map))

        # what squares do we search
        adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0),)
        if self.allow_diagonal_movement:
            adjacent_squares = ((0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1),)

        # Loop until you find the end
        while len(open_list) > 0:
            outer_iterations += 1

            if outer_iterations > max_iterations:
                # if we hit this point return the path such as it is
                # it will not contain the destination
                print("giving up on pathfinding too many iterations")
                return self.return_path(current_node)
            
            # Get the current node
            current_node = heapq.heappop(open_list)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                return self.return_path(current_node)

            # Generate children
            children = []
            
            for new_position in adjacent_squares: # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(self.map) - 1) or node_position[0] < 0 or node_position[1] > (len(self.map[len(self.map)-1]) -1) or node_position[1] < 0:
                    continue

                # Make sure walkable terrain
                if self.map[node_position[0]][node_position[1]]:
                    continue

                # Create new node
                new_node = Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:
                # Child is on the closed list
                if len([closed_child for closed_child in closed_list if closed_child == child]) > 0:
                    continue

                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = ((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)
                child.f = child.g + child.h

                # Child is already in the open list
                if len([open_node for open_node in open_list if child.position == open_node.position and child.g > open_node.g]) > 0:
                    continue

                # Add the child to the open list
                heapq.heappush(open_list, child)
        
        print("Couldn't get a path to destination")
        return None
