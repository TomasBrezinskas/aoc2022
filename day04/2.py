t_sum = 0
for line in open('input.txt'):
    cut = line.strip().split(",")
    a = [eval(i) for i in cut[0].split("-")]
    b = [eval(i) for i in cut[1].split("-")]

    if (a[0] <= b[0] <= a[1]) or (a[0] <= b[1] <= a[1]) or (b[0] <= a[0] <= b[1]) or (b[0] <= a[1] <= b[1]):
        t_sum += 1

print(t_sum)
