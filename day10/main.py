data = open('input.txt').read().strip().split('\n')
temp_str = 1
counter = 0
max_str = 0
crt = [["." for _ in range(40)] for _ in range(6)]


def do_cycle():
    global counter, max_str, temp_str
    counter += 1
    if counter in (20, 60, 100, 140, 180, 220):
        max_str += counter * temp_str
    if abs((counter - 1) % 40 - temp_str) < 2:
        crt[(counter - 1) // 40][(counter - 1) % 40] = '#'


for line in data:
    if line == 'noop':
        do_cycle()
    else:
        do_cycle()
        do_cycle()
        temp_str += int(line.split()[1])

print(max_str)  # part 1

for line in crt:
    print("".join(line))  # part 2
