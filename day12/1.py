import collections
import numpy as np

data = [list(x.strip()) for x in open("input.txt").readlines()]
elevations = np.array([[ord(char) - ord('a') for char in line] for line in data])

source = tuple(x[0] for x in np.where(elevations == ord('S') - ord('a')))
target = tuple(x[0] for x in np.where(elevations == ord('E') - ord('a')))

elevations[source] = 0
elevations[target] = 25

x_max, y_max = elevations.shape

seen = set()
result = 0

active = collections.deque([(0, source)])

while active:
    steps, current = active.popleft()
    if current == target:
        result = steps
        break
    if current in seen:
        continue

    seen.add(current)

    candidates = [(current[0] - 1, current[1]), (current[0] + 1, current[1]),
                  (current[0], current[1] - 1), (current[0], current[1] + 1)]

    filtered = [c for c in candidates if 0 <= c[0] < x_max and 0 <= c[1] < y_max]

    neighbors = [n for n in filtered if elevations[n] - elevations[current[0], current[1]] <= 1]

    for neighbor in neighbors:
        active.append((steps + 1, neighbor))

print(result)
