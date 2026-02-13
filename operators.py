# This file contains the operations that can be performed on the puzzle board.

# Function to create a new board state by swapping two tiles.
def swap_tiles(state, index_one, index_two):
    # Copy the current state list so we do not change the original one.
    new_state = list(state)
    
    # Store the value of the first tile temporarily.
    temp_value = new_state[index_one]
    
    # Move the second tile into the first tile's position.
    new_state[index_one] = new_state[index_two]
    
    # Move the stored temporary value into the second tile's position.
    new_state[index_two] = temp_value
    
    # Return the newly created state.
    return new_state

# Function to determine which directions the blank tile can move.
def get_possible_moves(blank_index):
    # Store the results in a list of (direction, target_index) pairs.
    valid_moves = []
    
    # Convert the 1D index to 2D coordinates (for a 3x3 grid).
    row = blank_index // 3
    col = blank_index % 3
    
    # Check if moving UP is possible (not in the top row).
    if row > 0:
        target_index = blank_index - 3
        valid_moves.append(("Up", target_index))
        
    # Check if moving DOWN is possible (not in the bottom row).
    if row < 2:
        target_index = blank_index + 3
        valid_moves.append(("Down", target_index))
        
    # Check if moving LEFT is possible (not in the first column).
    if col > 0:
        target_index = blank_index - 1
        valid_moves.append(("Left", target_index))
        
    # Check if moving RIGHT is possible (not in the last column).
    if col < 2:
        target_index = blank_index + 1
        valid_moves.append(("Right", target_index))
        
    return valid_moves
