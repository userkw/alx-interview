#!/usr/bin/python3
"""
Define island_perimeter
"""

bound_4 = set()
bound_3 = set()
bound_2 = set()
bound_1 = set()


def boundary(grid, a, j):
    """Find cells
       Args:
           grid (list): 2d list
           a (int): row number
           j (int): column number
    """
    boundaries = 0
    try:
        if a == 0:
            boundaries += 1
        elif grid[a-1][j] == 0:
            boundaries += 1
    except:
        boundaries += 1
    try:
        if grid[a+1][j] == 0:
            boundaries += 1
    except:
        boundaries += 1
    try:
        if grid[a][j+1] == 0:
            boundaries += 1
    except:
        boundaries += 1
    try:
        if j == 0:
            boundaries += 1
        elif grid[a][j-1] == 0:
            boundaries += 1
    except:
        boundaries += 1

    if boundaries == 1:
        bound_1.add((a, j))
    elif boundaries == 2:
        bound_2.add((a, j))
    elif boundaries == 3:
        bound_3.add((a, j))
    elif boundaries == 4:
        bound_4.add((a, j))


def island_perimeter(grid):
    """
    Calculate
    Args:
        grid [list] : 2d list of ints either 0 or 1
    Return:
       perimeter of island
    """
    if grid == []:
        return 0
    l = len(grid)
    w = len(grid[0])
    for a in range(l):
        for j in range(w):
            if grid[a][j] == 1:
                boundary(grid, a, j)
                if len(bound_4) != 0:
                    return 4
    perimeter = (len(bound_3) * 3) + (len(bound_2) * 2) + (len(bound_1))
    return perimeter
