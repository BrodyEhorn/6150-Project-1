import operators
import heuristics

class Node:
    # Function to set all the initial values for a new node.
    def initialize_node_data(self, state, parent=None, action=None, swapped_number=None, g=0, h=0):
        # The current configuration of the board.
        self.state = state
        
        # The node that generated this node.
        self.parent = parent
        
        # The action taken to reach this state (e.g., 'Up', 'Down').
        self.action = action
        
        # The number that the blank tile (0) swapped with.
        self.swapped_number = swapped_number
        
        # g is the cost to reach this node from the start state.
        self.g = g
        
        # h is the estimated cost from this node to the goal state.
        self.h = h
        
        # f is the total estimated cost (g + h).
        self.f = self.g + self.h

    # Function to compare f-costs for sorting nodes in the priority queue.
    def compare_f_cost(self, other):
        return self.f < other.f

# Function to find the index of the blank tile (marked as 0).
def find_blank_tile_index(state):
    # Search the list for the value 0.
    return state.index(0)

# Function to print the board state in a readable 3x3 grid format.
def display_board_grid(state):
    # Print each row of the board one by one.
    
    # Row 1.
    print(state[0], state[1], state[2])
    
    # Row 2.
    print(state[3], state[4], state[5])
    
    # Row 3.
    print(state[6], state[7], state[8])

# Function to trace back from the goal node and display the full path of moves.
def display_solution_path(goal_node):
    # This list will store the sequence of nodes from goal back to start.
    path = []
    current = goal_node
    
    # Backtrack using the parent pointers.
    while current is not None:
        path.append(current)
        current = current.parent
        
    # Reverse the list to get the path from start to goal.
    path.reverse()
    
    # We skip the first node (index 0) because it's the initial state.
    print("\n--- SOLUTION PATH ---")
    for i in range(1, len(path)):
        node = path[i]
        print(f"\nStep {i}: Move 0 {node.action} (swapped with {node.swapped_number})")
        display_board_grid(node.state)
    print("\n---------------------")

# Function to find and remove the node with the lowest f-cost from the open list.
def select_best_node(open_list):
    # Start by assuming the first node has the lowest f-cost.
    best_node = open_list[0]
    best_index = 0
    
    # Check all other nodes in the list.
    for i in range(1, len(open_list)):
        # If we find a node with a lower f-cost, update our best node.
        if open_list[i].f < best_node.f:
            best_node = open_list[i]
            best_index = i
            
    # Remove the best node from the list and return it.
    return open_list.pop(best_index)

# Function to perform the A* search algorithm to solve the puzzle.
def perform_a_star_search(initial_state, goal_state, heuristic_function):
    # The open list is a standard list of nodes to be explored.
    open_list = []
    
    # The visited set stores states we have already expanded to avoid cycles.
    visited_states = set()
    
    # Metrics to track the search progress.
    nodes_generated = 0
    nodes_expanded = 0
    
    # Create the starting node.
    start_node = Node()
    nodes_generated += 1
    
    # Calculate initial heuristic cost.
    h_init = heuristic_function(initial_state, goal_state)
    
    # Initialize the starting node's data.
    # g (distance from start) is 0 for the beginning node.
    start_node.initialize_node_data(
        state=initial_state,
        parent=None,
        action=None,
        swapped_number=None,
        g=0,
        h=h_init
    )
    
    # Add the starting node to the open list.
    open_list.append(start_node)
    
    # --- The Main A* Loop ---
    # We continue as long as there are nodes in the open list.
    while open_list:
        # 1. Select the node with the lowest f-cost.
        current_node = select_best_node(open_list)
        nodes_expanded += 1
        
        # Print progress to show which move the computer is considering.
        print(f"\n--- Exploring Node (f={current_node.f}, g={current_node.g}, h={current_node.h}) ---")
        display_board_grid(current_node.state)
        
        # 2. Mark this state as visited.
        visited_states.add(tuple(current_node.state))
        
        # 3. Find where the blank tile is.
        blank_index = find_blank_tile_index(current_node.state)
        
        # 4. Get the possible moves from this position.
        possible_moves = operators.get_possible_moves(blank_index)
        
        # 5. Expand this node by checking all possible moves.
        for direction, target_index in possible_moves:
            # Generate the new board state.
            new_state = operators.swap_tiles(current_node.state, blank_index, target_index)
            
            # Skip this move if we've already expanded this state before.
            if tuple(new_state) in visited_states:
                continue
            
            # Get the number we swapped with.
            swapped_with = current_node.state[target_index]
            
            # Create the child node.
            child_node = Node()
            nodes_generated += 1
            
            # Calculate costs for the child node.
            new_g = current_node.g + 1
            new_h = heuristic_function(new_state, goal_state)
            
            print(f"  Option: Move 0 {direction} (swaps with {swapped_with}), f = {new_g + new_h} (g: {new_g} + h: {new_h})")
            
            # Initialize the child node.
            child_node.initialize_node_data(
                state=new_state,
                parent=current_node,
                action=direction,
                swapped_number=swapped_with,
                g=new_g,
                h=new_h
            )
            
            # Add the child node to the open list to be explored later.
            open_list.append(child_node)
            
            # 6. Check if this child is the goal.
            if child_node.h == 0:
                print(f"  Goal found! (State matches the goal layout)")
                return child_node, open_list, nodes_generated, nodes_expanded, True
        
        # Safety break to prevent infinite loops during testing if something goes wrong.
        if nodes_expanded > 1000:
            print("\nError: Search limit (1000 expansions) reached. Stopping safety loop.")
            break
            
    # If the loop ends and no goal is found.
    return None, open_list, nodes_generated, nodes_expanded, False

# Function to collect and validate a board state from the user.
def get_board_input(board_name):
    while True:
        print(f"\nEnter the {board_name} row by row (3 numbers with spaces between them, 0 for blank):")
        
        state = []
        for i in range(3):
            while True:
                row_input = input(f"Enter Row {i + 1} (3 numbers): ")
                try:
                    row_data = [int(x) for x in row_input.split()]
                    if len(row_data) != 3:
                        print("Error: Please enter exactly 3 numbers for the row.")
                        continue
                    state.extend(row_data)
                    break
                except ValueError:
                    print("Error: Please enter only numbers separated by spaces.")
                    continue
        
        # Check if the board is valid (contains 0-8 exactly once).
        if sorted(state) == list(range(9)):
            return state
        else:
            print(f"\nError: The {board_name} must contain all numbers from 0 to 8 exactly once.")
            print("Please try again.\n")

# The main function to test the current logic.
def main():
    # Get the initial board state.
    state = get_board_input("Initial Board State")
    
    # Get the goal board state.
    goal_state = get_board_input("Goal Board State")
    
    # Print the current board state.
    print("\nCurrent Board State:")
    display_board_grid(state)
    
    # Print the goal state.
    print("\nGoal State:")
    display_board_grid(goal_state)
    
    # Find the blank tile.
    blank_index = find_blank_tile_index(state)
    
    # Calculate Misplaced Tiles (H1) and Manhattan Distance (H2).
    h1_score = heuristics.calculate_misplaced_tiles(state, goal_state)
    h2_score = heuristics.calculate_manhattan_distance(state, goal_state)
    
    # Print the result.
    print(f"\nThe blank tile (0) is at index: {blank_index}")
    print(f"Heuristic 1 (Misplaced Tiles): {h1_score}")
    print(f"Heuristic 2 (Manhattan Distance): {h2_score}")

    # Test the start of the A* search.
    last_node, open_list, gen_count, exp_count, goal_found = perform_a_star_search(state, goal_state, heuristics.calculate_manhattan_distance)
    
    if goal_found:
        print(f"\n--- SUCCESS: Goal Reached ---")
        display_solution_path(last_node)
    else:
        print(f"\n--- FAILURE: Goal NOT Reached ---")
    
    print(f"\nSearch Metrics:")
    print(f"Total Nodes Generated: {gen_count}")
    print(f"Total Nodes Expanded: {exp_count}")
    print(f"Nodes currently in the open list: {len(open_list)}")

# Start the program.
if __name__ == "__main__":
    main()
