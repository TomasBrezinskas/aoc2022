data = open('input.txt').readline()
print(min([n+14 for n in range(len(data)) if len(set(data[n:n+14])) == 14]))
