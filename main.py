#!/usr/bin/env python3

from collections import deque

def get(puzzle, x, y):
    return puzzle[x + y * 3]

def toggle(puzzle, x, y):
    r = list(puzzle)
    r[x + y * 3] = 1 - r[x + y * 3]
    return tuple(r)


def walk_on(puzzle, x, y):
    puzzle = toggle(puzzle, x, y)
    if x > 0:
        puzzle = toggle(puzzle, x - 1, y)
    if y > 0:
        puzzle = toggle(puzzle, x, y - 1)
    if x < 2:
        puzzle = toggle(puzzle, x + 1, y)
    if y < 2:
        puzzle = toggle(puzzle, x, y + 1)
    return puzzle

def count_around(puzzle, x, y):
    a = 0

    a += get(puzzle, x, y)
    if x > 0:
        a += get(puzzle, x - 1, y)
    if y > 0:
        a += get(puzzle, x, y - 1)
    if x < 2:
        a += get(puzzle, x + 1, y)
    if y < 2:
        a += get(puzzle, x, y + 1)

    return a

def print_puzzle(puzzle, msg = "Puzzle"):
    print("---------")
    print(msg)
    print(puzzle[0:3])
    print(puzzle[3:6])
    print(puzzle[6:9])
    print("---------")





solved = (
    1, 1, 1,
    1, 1, 1,
    1, 1, 1
)

puzzle = (
    1, 0, 1,
    0, 0, 0,
    1, 0, 1,
)

q = deque()
q.append((puzzle, (puzzle,)))
cache = set()

while len(q) > 0:
    (puzzle, trace) = q.popleft()
    if puzzle in cache:
        continue
    cache.add(puzzle)
    if puzzle == solved:
        for (step,p) in enumerate(trace):
            print_puzzle(p, f"Step {step}")
        break


    next_tries = []
    for x in range(0, 3):
        for y in range(0, 3):
            next_tries.append((x, y))

    next_tries.sort(key=lambda t: count_around(puzzle, t[0], t[1]))

    for (x, y) in next_tries:
        z = walk_on(puzzle, x, y)
        q.append((z, trace + (z,)))

