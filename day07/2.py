data = open('input.txt').read()
dirs = {'/': 0}
path = ['/']
for line in data.splitlines()[1:]:
    split = line.split(" ")
    if split[0] == '$':
        if split[1] == 'cd':
            if split[2] == '..':
                path.pop()
            else:
                path.append(split[2])
    elif split[0] == 'dir':
        dirs["".join(path) + split[1]] = 0
    else:
        dirs["".join(path)] += int(split[0])
        for i in range(1, len(path)):
            dirs["".join(path[:-i])] += int(split[0])

required = 30000000 - (70000000 - dirs['/'])
print(min(x for x in dirs.values() if x >= required))
