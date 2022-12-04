prio = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
t_sum = 0

rf = open('input.txt')
while True:
    a = rf.readline()
    b = rf.readline()
    c = rf.readline()

    if not a or not b or not c:
        break

    for char in a:
        if char in b:
            if char in c:
                t_sum += prio.index(char)
                break
    else:
        continue

print(t_sum)
