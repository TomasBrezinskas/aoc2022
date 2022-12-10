prio = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
t_sum = 0

for line in open('input.txt'):
    first = line[:len(line) // 2]
    second = line[len(line) // 2:]
    for char in first:
        if char in second:
            t_sum += prio.index(char)
            break

print(t_sum)
