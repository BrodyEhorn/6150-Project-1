# This file contains heuristic functions for the A* search algorithm.

# Function for Heuristic 1 (H1): The number of misplaced tiles.
def calculate_misplaced_tiles(state, goal):
    # The count of tiles that are not in their correct goal position.
    misplaced_count = 0
    
    # Iterate through each tile position.
    for i in range(len(state)):
        # Check if the tile is in the wrong place and is not the blank tile (0).
        # We generally do not count the blank tile in these heuristics.
        if state[i] != 0 and state[i] != goal[i]:
            misplaced_count += 1
            
    return misplaced_count

# Function for Heuristic 2 (H2): The sum of Manhattan distances of tiles.
def calculate_manhattan_distance(state, goal):
    # The total accumulated Manhattan distance for all tiles.
    total_distance = 0
    
    # Iterate through each number on the board (1 through 8).
    # We skip 0 because it's the blank tile.
    for number in range(1, 9):
        # Find where the number is in the current state.
        current_index = state.index(number)
        
        # Find where the number should be in the goal state.
        goal_index = goal.index(number)
        
        # Convert 1D indices to 2D (row, col) coordinates for a 3x3 grid.
        current_row = current_index // 3
        current_col = current_index % 3
        
        goal_row = goal_index // 3
        goal_col = goal_index % 3
        
        # Calculate the distance for this tile and add it to the total.
        # Manhattan distance = |row1 - row2| + |col1 - col2|
        distance = abs(current_row - goal_row) + abs(current_col - goal_col)
        total_distance += distance
        
    return total_distance
