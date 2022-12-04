most = 0
temp = 0
for line in open('input.txt'):
    if line.strip():
        temp += int(line)
    else:
        if temp > most:
            most = temp
        temp = 0
print(most)
