import numpy as np

# Returns the new coordinate after taking action
def step(action, coord):
    match action:
        case 0: # up
            return coord[0], coord[1]-1
        case 1: # down
            return coord[0], coord[1]+1
        case 2: # left
            return coord[0]-1, coord[1]
        case 3: # right
            return coord[0]+1, coord[1]
    return None # invalid action taken

# Checks if there are any possible steps
def isStuck(coord, visited):
    return (coord[0], coord[1]-1) in visited\
        and (coord[0], coord[1]+1) in visited\
        and (coord[0]-1, coord[1]) in visited\
        and (coord[0]+1, coord[1]) in visited

def generateSARW(n):
    actions = []
    coords = [(0,0)]
    visited = set([(0,0)])
    while len(actions) < n:
        action = np.random.randint(0, 4)
        if isStuck(coords[-1], visited): # Restarts the process
            actions = []
            coords = [(0,0)]
            visited = set([(0,0)])
        newCoord = step(action, coords[-1])
        if newCoord not in visited:
            actions.append(action)
            coords.append(newCoord)
            visited.add(newCoord)
    return coords, actions

if __name__ == '__main__':
    for i in range(10_000):
        generateSARW(50)


