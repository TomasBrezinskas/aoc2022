data = open('input.txt').read()
dirs = {'/': 0}
path = ['/']
for line in data.splitlines()[1:]:  # skipping first command as it's the only 'cd /'
    split = line.split(" ")
    if split[0] == '$':  # it's a command (ls is skipped)
        if split[1] == 'cd':
            if split[2] == '..':
                path.pop()
            else:
                path.append(split[2])
    elif split[0] == 'dir':
        dirs["".join(path) + split[1]] = 0  # want to avoid imports, so won't have '/' separator
    else:  # ls result                      # could use os.path.join method
        dirs["".join(path)] += int(split[0])
        for i in range(1, len(path)):
            dirs["".join(path[:-i])] += int(split[0])

print(sum(x for x in dirs.values() if x <= 100000))
