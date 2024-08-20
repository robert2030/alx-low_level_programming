#!/usr/bin/python3
"""Defines an island perimeter measuring function."""


def island_perimeter(grid):
    """
Constraints:
    - 0 represents a water zone, 1 represents a land zone.
    - One cell is a square with a side length of 1.
    - Grid cells are connected horizontally/vertically (not diagonally).
    - Grid is rectangular, with width and height not exceeding 100.
    - Grid is completely surrounded by water,
        with only one island (or nothing).
    - The island doesn’t have “lakes”
        (water inside that isn’t connected to the water around the island).
    """

    rows = len(grid)
    cols = len(grid[0]) if rows else 0
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4

                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1

                if i < rows - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1

                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1

                if j < cols - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1

    return perimeter
