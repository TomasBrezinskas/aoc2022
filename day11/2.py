import time
import re

start = time.time()

digit_regex = r'\d+'
monkeys = open('input.txt').read().strip().split('\n\n')
tests = []
rounds = 10000

for i, monkey in enumerate(monkeys):
    line = [x.strip() for x in monkey.split("\n")]
    starting_items = list(map(int, list(re.findall(digit_regex, line[1]))))
    _, operation = line[2].split('=')
    tests.append(int(re.findall(digit_regex, line[3])[0]))
    monkey_if_true = int(line[4][-1])
    monkey_if_false = int(line[5][-1])
    monkeys[i] = [starting_items, operation, monkey_if_true, monkey_if_false, 0]  # 0 will be used as counter

for i, monkey in enumerate(monkeys):  # replace items with lcm list
    olds = monkey[0]
    new = []
    for old in olds:
        new.append([old % tests[i] for i in range(len(monkeys))])
    monkeys[i][0] = new

for _ in range(rounds):
    for i, monkey in enumerate(monkeys):
        items, operation, if_true, if_false, count = monkey
        while items:
            item = items.pop(0)
            new = []

            for j, h in enumerate(item):
                res = operation.replace('old', str(h))
                res = eval(res) % tests[j]
                new.append(res)

            if new[i] % tests[i] == 0:
                monkeys[if_true][0].append(new)
            else:
                monkeys[if_false][0].append(new)
            count += 1
        monkeys[i] = [[], operation, if_true, if_false, count]

activity = [monkey[-1] for monkey in monkeys]
activity.sort()
monkey_business = int(activity[-1]) * int(activity[-2])
print(monkey_business)
print("execution time: " + str(time.time() - start))  # 17.40 seconds on my machine
