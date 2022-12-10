input_data = open("input.txt").read()
# \n\n marks split between stack and instructions
stack_input, instructions = [part.split("\n") for part in input_data.split("\n\n")]

# reformat stack_input into usable thing
cols = len([x for x in stack_input[-1].split(" ") if x])
stack = [""] * (cols+1)  # cols+1 so we will have the stack[0] element empty for simpler use later
for line in stack_input[:-1]:
    for i, box in enumerate(line[1::4]):
        if box != " ":
            stack[i + 1] += box

# do instructions
for line in instructions:
    _, n, _, src, _, dest = line.split()  # only need number / source / destination
    n, src, dest = int(n), int(src), int(dest)
    stack[src], stack[dest] = stack[src][n:], stack[src][:n][::-1] + stack[dest]  # need to reverse for proper order

# print only first
print("".join(x[0] for x in stack if x))
