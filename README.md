# 8-Puzzle Solver

This project implements an AI solver for the classic 8-puzzle game using the A* search algorithm.

## Files
- `solver.py`: The main entry point. Contains the search loop, user interface, and path display.
- `operators.py`: Move logic (up, down, left, right) and board manipulation.
- `heuristics.py`: Heuristic functions (Misplaced Tiles and Manhattan Distance).
- `Project_Report.txt`: Detailed technical documentation of the implementation.

## Prerequisites
- Python 3.x installed on your system.

## How to Run
1. Open a terminal or command prompt.
2. Navigate to the project directory.
3. Run the following command:
   ```bash
   python solver.py
   ```

## How to Input the Board
The program will ask you to enter the board state row by row.
- Use numbers **1-8** for tiles.
- Use **0** for the blank space.
- Separate the three numbers in each row with **spaces**.

### Example Input:
```text
Enter Row 1 (3 numbers): 1 2 3
Enter Row 2 (3 numbers): 4 5 6
Enter Row 3 (3 numbers): 7 0 8
```

## Features
- **A* Search**: Efficiently finds the shortest solution.
- **Cycle Prevention**: Uses a visited set to avoid infinite loops.
- **Search Metrics**: Tracks total nodes generated and expanded.
- **Path Reconstruction**: Displays the step-by-step grid layouts from the start to the goal.
