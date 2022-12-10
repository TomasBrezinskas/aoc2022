data = open('input.txt').readline()
print(min([n+4 for n in range(len(data)) if len(set(data[n:n+4])) == 4]))
