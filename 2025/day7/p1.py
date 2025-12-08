from collections import deque

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
    split_beams = set()
    splits = set()
    split_count = 0
    while beams:

        beam_pos = beams.popleft()
        next_pos = get_down(grid, beam_pos)
        if not next_pos:
            continue

        cell = grid[next_pos[0]][next_pos[1]]
        if cell == SPLITTER:
            left = get_left(grid, next_pos)
            right = get_right(grid, next_pos)

            if next_pos not in split_beams:
                split_count += 1
                splits.add(next_pos)

            if left and left not in split_beams:
                beams.append(left)
                split_beams.add(left)
            if right and right not in split_beams:
                beams.append(right)
                split_beams.add(right)

        else:
            beams.appendleft(next_pos)

    return splits, split_beams, split_count

with open("day7.txt", 'r') as f:

    block = f.read().splitlines()

    grid = as_grid(block)

    start = find_start(grid)

    splits, split_beams, split_count = execute_beams(grid, start)
    split_dict = dict()
    for split in splits:
        split_dict[split] = '|'

    print_grid(grid, split_dict)

    print(f"Day 7-1: {len(splits)}")