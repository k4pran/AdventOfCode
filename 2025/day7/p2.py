# from collections import deque
#
# from sympy.testing.runtests import split_list
#
# from data.grid import *
#
# START = 'S'
# SPLITTER = '^'
#
# def find_start(grid):
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j] == START:
#                 return i, j
#
# def execute_beams(grid, start):
#
#     beams = deque([start])
#     split_count = 0
#     visited = set()
#     # paths = set()
#     # path = []
#     while beams:
#
#         beam_pos = beams.popleft()
#         print(beam_pos)
#         # path.append(beam_pos)
#
#         next_pos = get_down(grid, beam_pos)
#         if not next_pos:
#             # paths.add(tuple(path))
#             # print(path)
#             # path = []
#             # if tuple(path) in paths:
#             #     raise ValueError
#             # split_count += 1
#             # if beams:
#             #     beams.append(beams.popleft())
#             continue
#
#         cell = grid[next_pos[0]][next_pos[1]]
#         if cell == SPLITTER:
#             left = get_left(grid, next_pos)
#             right = get_right(grid, next_pos)
#
#
#             if next_pos not in visited:
#                 split_count += 2
#                 visited.add(next_pos)
#
#
#             if left:
#                 visited.add((beam_pos, next_pos, "L"))
#                 beams.append(left)
#
#             if right:
#                 visited.add((beam_pos, next_pos, "R"))
#                 beams.append(right)
#
#         else:
#             beams.append(next_pos)
#
#     return split_count
#
# with open("day7.txt", 'r') as f:
#
#     block = f.read().splitlines()
#
#     grid = as_grid(block)
#
#     start = find_start(grid)
#
#     split_count = execute_beams(grid, start)
#     split_dict = dict()
#     # for split in splits:
#     #     split_dict[split] = '|'
#
#     print_grid(grid, split_dict)
#
#     ## 3132 too low
#
#     print(f"Day 7-2: {split_count}")


from collections import deque

from sympy.testing.runtests import split_list

from data.grid import *

START = 'S'
SPLITTER = '^'

def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == START:
                return i, j

def execute_beams(grid, start):

    beams = deque([start])
    split_count = 0
    visited = set()
    while beams:

        beam_pos = beams.popleft()
        print(beam_pos)

        next_pos = get_down(grid, beam_pos)
        if not next_pos:
            continue

        cell = grid[next_pos[0]][next_pos[1]]
        if cell == SPLITTER:
            left = get_left(grid, next_pos)
            right = get_right(grid, next_pos)


            if next_pos not in visited:
                split_count += 2
                visited.add(next_pos)


            if left:
                visited.add((beam_pos, next_pos, "L"))
                beams.append(left)

            if right:
                visited.add((beam_pos, next_pos, "R"))
                beams.append(right)

        else:
            beams.append(next_pos)

    return split_count

with open("day7.txt", 'r') as f:

    block = f.read().splitlines()

    grid = as_grid(block)

    start = find_start(grid)

    split_count = execute_beams(grid, start)
    split_dict = dict()


    print_grid(grid, split_dict)

    print(f"Day 7-2: {split_count}")
