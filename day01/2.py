array = []
temp = 0
for line in open('input.txt'):
    if line.strip():
        temp += int(line)
    else:
        array.append(temp)
        temp = 0
print(sum(sorted(array)[::-1][0:3]))
