data = open('input.txt').read().splitlines()
height, width = len(data), len(data[0])
visible_trees = set()
highest_score = 0

for y in range(height):
    for x in range(width):
        tree = data[y][x]

        left = data[y][:x][::-1]
        right = data[y][x + 1:width]
        up = [data[ny][x] for ny in range(y)[::-1]]
        down = [data[ny][x] for ny in range(y + 1, height)]

        score = 1
        for direction in left, down, up, right:
            for i, neighbour in enumerate(direction):
                if tree <= neighbour:
                    score *= i + 1
                    break
            else:
                score *= len(direction) if direction else 1
                visible_trees.add((x, y))
        highest_score = max(highest_score, score)

print(len(visible_trees))
print(highest_score)
