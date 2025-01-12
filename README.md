# Sliding Puzzle Solver

This project implements a basic solver for a 3x3 sliding puzzle (also known as the 8-puzzle). The goal is to rearrange the tiles in the puzzle from a starting configuration to a specified goal configuration by sliding tiles into an empty space.

## Features
- **Puzzle Input**: Users can input a starting and ending matrix for the puzzle, with `-1` representing the blank space.
- **Heuristic Calculation**: A Manhattan Distance heuristic is used to calculate the cost of reaching the goal state.
- **Automated Solver**: The program attempts to solve the puzzle using the heuristic to decide the best move at each step.
- **Visualization**: Prints the puzzle matrix and tracks the number of iterations required to solve the puzzle.

---

## Prerequisites
- Python 3.x

---

## How to Use

1. Clone or download the repository to your local machine.
2. Run the program:
   ```bash
   python sliding_puzzle_solver.py
   ```
3. Follow the prompts to input the initial and goal configurations of the puzzle:
   - Enter integers from `1` to `8` for the tiles and `-1` for the blank space.
   - Ensure that all numbers from `1` to `8` are used exactly once, and `-1` is used once.

Example input for a 3x3 puzzle:
```
Input numbers: 1 2 3
Input numbers: 4 5 6
Input numbers: 7 8 -1
```

---

## Example Run

**Input:**
```
Starting Puzzle:
1 2 3
4 5 6
7 8 -1

Goal Puzzle:
1 2 3
4 5 6
7 -1 8
```

**Output:**
```
Number of counts: 1
Heuristic value: 0
1 2 3
4 5 6
7 -1 8
```

---

## Code Structure

- **`populate()`**  
  Prompts the user to input a valid 3x3 puzzle configuration. Ensures all numbers are unique and valid.
  
- **`calculate_distance_to_goal(matrix_start, matrix_end)`**  
  Computes the Manhattan Distance between the current puzzle state and the goal state.

- **`print_matrix(matrix)`**  
  Nicely formats and prints a 3x3 puzzle matrix.

- **`main()`**  
  Implements the solving logic using the Manhattan Distance heuristic to determine the best moves. The solver iteratively updates the puzzle state and prints the solution trace.

---

## Limitations
- The heuristic and solving logic may not be optimal for all configurations.
- The program does not currently handle unsolvable puzzles.
- Input validation is limited; users must ensure correct input manually.

---

## Future Enhancements
- Add checks for unsolvable puzzles based on inversion count.
- Optimize move selection using advanced search algorithms (e.g., A*).
- Improve input validation and error handling.
- Add graphical representation of the puzzle.

---

## License
This project is open source and available under the [MIT License](LICENSE).

