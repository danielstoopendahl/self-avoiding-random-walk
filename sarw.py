import numpy as np
import random

# Returns a list of possible next coordinates
def get_candidates(coord, visited):
    candidates = []
    up = (coord[0], coord[1]-1)
    down = (coord[0], coord[1]+1)
    left = (coord[0]-1, coord[1])
    right = (coord[0]+1, coord[1])
    if up not in visited: candidates.append(up)
    if down not in visited: candidates.append(down)
    if left not in visited: candidates.append(left)
    if right not in visited: candidates.append(right)
    return candidates

def generate_SARW(n):
    coords = [(0,0)]
    visited = set(coords)
    while len(coords) <= n:
        candidates = get_candidates(coords[-1], visited)
        if len(candidates) == 0:
            coords = [(0,0)]
            visited = set(coords)
        coords.append(random.choice(candidates))
    return coords

if __name__ == '__main__':
    # test speed of implementation
    for i in range(100_000):
        generate_SARW(50)
    # smoke test for correctness
    print(generate_SARW(10))

