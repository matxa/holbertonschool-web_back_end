#!/usr/bin/python3
"""perimeter of the island described in grid:"""


def island_perimeter(grid):
    """island_perimeter - perimeter of the island"""
    """island_perimeter - perimeter of the island
    Parameter
    ---------
    grid:
    list
    Return
    ------
    int
    """
    total = 0

    rows = len(grid)
    columns = len(grid[0])

    for row in range(rows):
        for col in range(columns):
            array = grid[row][col]
            if array == 1:
                total += 4
                if row != 0 and grid[row-1][col] == 1:
                    total -= 1
                if col != 0 and grid[row][col-1] == 1:
                    total -= 1
                if row + 1 != rows and grid[row + 1][col] == 1:
                    total -= 1
                if col + 1 != columns and grid[row][col + 1] == 1:
                    total -= 1

    return total
