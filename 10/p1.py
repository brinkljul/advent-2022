with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    lines = [x.split() for x in lines]
    commands = [[line[0], int(line[1])] if len(line) == 2 else [line[0]] for line in lines]

x = 1
cycles = 0
res = 0
for command in commands:
    print(command)
    if command[0] == "noop":
        cycles += 1
        if (cycles + 20) % 40 == 0: res += x * cycles
    elif command[0] == "addx":
        cycles += 1
        if (cycles + 20) % 40 == 0: res += x * cycles
        cycles += 1
        if (cycles + 20) % 40 == 0: res += x * cycles
        x += command[1]

print(res)