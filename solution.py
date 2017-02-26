from utils import *
import logging


def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    logging.debug("Naked twins started")
    # Iterating over units
    for unit in unitlist:

        # Finding unsolved boxes of length 2
        candidate_boxes = [box for box in unit if len(values[box]) == 2]
        twins = []

        # Looking for twins in candidate boxes
        for i in range(len(candidate_boxes) - 1):
            twins = [(candidate_boxes[i], candidate_boxes[j]) for j in range(i + 1, len(candidate_boxes))
                     if values[candidate_boxes[i]] == values[candidate_boxes[j]]]

        # Eliminating the naked twins as possibilities for their peers
        for twin in twins:
            for box in unit:
                if box in twin:     # do not change twins themselves
                    continue

                for digit in values[twin[0]]:
                    # removing possibility (digit) from peer box
                    assign_value(values, box, values[box].replace(digit, ''))

    return values

def eliminate(values):
    """
    Go through all the boxes, and whenever there is a box with a value, eliminate this value from the values of all its peers.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """

    logging.debug("Eliminate started.")
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            assign_value(values, peer, values[peer].replace(digit,''))
    return values


def only_choice(values):
    """
    Go through all the units, and whenever there is a unit with a value that only fits in one box, assign the value to this box.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """

    logging.debug("Only choice started.")
    for unit in unitlist:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                assign_value(values,dplaces[0], digit)
    return values


def reduce_puzzle(values):
    """
    Iterate eliminate() and only_choice(). If at some point, there is a box with no available values, return False.
    If the sudoku is solved, return the sudoku.
    If after an iteration of both functions, the sudoku remains the same, return the sudoku.
    Input: A sudoku in dictionary form.
    Output: The resulting sudoku in dictionary form.
    """

    logging.debug("Puzzle reduction ...")
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            logging.debug("Incorrect path.")
            return False
    return values


def search(values):
    "Using depth-first search and propagation, try all possible values."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)
    if values is False:
        return False  ## Failed earlier
    if all(len(values[s]) == 1 for s in boxes):
        return values  ## Solved!
    # Choose one of the unfilled squares with the fewest possibilities
    n, s = min((len(values[s]), s) for s in boxes if len(values[s]) > 1)

    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        logging.debug("New assignment: " + s + " : " + value)
        assign_value(new_sudoku, s, value)
        attempt = search(new_sudoku)
        if attempt:
            return attempt


def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = search(values)

    unsolved_boxes = [box for box in boxes if len(values[box])>1]
    if len(unsolved_boxes) > 0:
        values = False

    return values


if __name__ == '__main__':

    logging.basicConfig(level=logging.ERROR)

    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'

    logging.info("Starting solving Diagonal Sudoku")

    display(solve(diag_sudoku_grid))

    logging.info("Finished")

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
