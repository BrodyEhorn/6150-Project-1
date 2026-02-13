# 8-Puzzle Solver

This project implements a solver for the classic 8-puzzle game using the A* search algorithm.

## Files
- solver.py: The main entry point. Contains the search loop, user interface, and path display.
- operators.py: Move logic (up, down, left, right) and board manipulation.
- heuristics.py: Heuristic functions (Misplaced Tiles and Manhattan Distance).

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:

   python solver.py

## How to Input the Boards
The program will ask you to enter both the Initial Board State and the Goal Board State row by row.
- Use numbers 1-8 for tiles.
- Use 0 for the blank space.
- Separate the three numbers in each row with spaces.

### Example Input:
Enter Row 1 (3 numbers): 1 2 3
Enter Row 2 (3 numbers): 4 5 6
Enter Row 3 (3 numbers): 7 0 8

### Example Input Flow:
1. Enter Initial Board State.
2. Enter Goal Board State.

