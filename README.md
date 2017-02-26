# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: The naked twins is another strategy that reduces domain(possible digits) for variables (boxes) in a particular unit. 
  The idea behind this strategy is that we are looking for two boxes that have two same possible values in a unit. We know that
  these two possibilities can only be assigned to one of these two boxes. Therefore, we eliminate these values from other 
  boxes in the same unit. Other two strategies that we implemented before, namely, 'eliminate' and 'only choice', cannot 
  find such cases, since they are looking for other types of inconsistencies.
  We apply this strategy in a loop ('reduce_puzzle' method) where all strategies are applied, to maximally 
  reduce puzzle before applying search algorithm. Adding another strategy, like 'naked twins',  that propagates constraints 
  increases chances of puzzle being solved before first assignment in a search process. In general, the more constraint
  propagation strategies we apply repeatedly as a preprocessing step (or propagation step), the better. This is because,
  whenever we solve an inconsistency using a particular strategy, a new inconsistency can arise that can be solved by
   another strategy, or even the same strategy.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: We solve digonal sudoku using the same approach (repeatedly apply reduction and search steps) that we use to solve
 normal one. The main difference between normal and diagonal sudoku, is that latter introduces two more constraints
 (numbers 1 to 9 appear exactly once on main diagonals). Having more constraints on the same amount of variables 
 makes them harder to satisfy. As a results, we could have more false paths, that do not lead to a solution, during a 
 search process. Which in turn, obviously, increases algorithms execution time. 
 In terms of the code, to make the additional constraints we define diagonal units ('diag_unit') in the code and 
 add them to the list of units. I do not make any other explicit changes to the code, since it is organized in such 
 a way that it automatically applies all defined constraints.
 

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