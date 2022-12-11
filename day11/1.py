import re

digit_regex = r'\d+'
monkeys = open('input.txt').read().strip().split('\n\n')
tests = []
rounds = 20  # can change to 10000 to invoke despair

for i, monkey in enumerate(monkeys):
    line = [x.strip() for x in monkey.split("\n")]
    starting_items = list(map(int, list(re.findall(digit_regex, line[1]))))
    operation = line[2].split()[-2:]
    tests.append(int(re.findall(digit_regex, line[3])[0]))
    monkey_if_true = int(line[4][-1])
    monkey_if_false = int(line[5][-1])
    monkeys[i] = [starting_items, operation, monkey_if_true, monkey_if_false, 0]  # 0 will be used as counter

for _ in range(rounds):
    for i, monkey in enumerate(monkeys):
        items, operation, if_true, if_false, count = monkey
        while items:
            item = items.pop(0)
            new = 0
            if operation[1] == 'old':
                if operation[0] == '+':
                    new = item * 2
                else:
                    new = pow(item, 2)
            else:
                if operation[0] == '+':
                    new = item + int(operation[1])
                else:
                    new = item * int(operation[1])
            if new % tests[i] == 0:
                monkeys[if_true][0].append(new)
            else:
                monkeys[if_false][0].append(new)
            count += 1
        monkeys[i] = [[], operation, if_true, if_false, count]

activity = [monkey[-1] for monkey in monkeys]
activity.sort()
monkey_business = int(activity[-1]) * int(activity[-2])
print(monkey_business)
