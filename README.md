# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twins is another strategy that reduces domain(possible digits) for variables (boxes) in a particular unit.
  I apply this strategy ia a main loop ('reduce_puzzle' method) where all strategies are applied including search.
  In general, to implement this strategy I iterate over all units and look for a boxes that have equal values of 
  lenght 2. After that I remove values of naked twins from other boxes in the unit.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: Diagonal Sudoku adds two more AllDiff constraints to existing 27 row, column, and 3x3 square AllDiffs.
 I do this by defining diagonal units ('diag_unit') and add them to the list of units. I do not make any other explicit 
      changes to the code, since it is organized in such a way that it automatically applies all defined constraints. 

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.