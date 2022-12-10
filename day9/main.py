def sign(x):
    return 1 if x > 0 else (-1 if x < 0 else 0)


data = open('input.txt').read().split("\n")
moves = {'R': (1, 0), 'U': (0, 1), 'L': (-1, 0), 'D': (0, -1)}
knot_amount = 2  # for part2 2 -> 10
rope = [(0, 0)] * knot_amount
visited = set()

for line in data:
    direction, steps = line.split()
    steps = int(steps)

    for _ in range(steps):
        hx, hy = rope[0]
        dx, dy = moves[direction]
        rope[0] = hx + dx, hy + dy

        for i in range(knot_amount-1):
            hx, hy = rope[i]
            tx, ty = rope[i + 1]
            dx, dy = hx - tx, hy - ty

            if pow(dx, 2) + pow(dy, 2) >= 4:
                rope[i + 1] = tx + sign(dx), ty + sign(dy)

        visited.add(tuple(rope[knot_amount-1]))

print(len(visited))

