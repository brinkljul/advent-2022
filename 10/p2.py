with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    lines = [x.split() for x in lines]
    commands = [[line[0], int(line[1])] if len(line) == 2 else [line[0]] for line in lines]

display = [['_' for _ in range(40)] for _ in range(6)]
x = 1
cycles = 0
res = 0
for command in commands:
    if command[0] == "noop":
        display[cycles // 40][cycles % 40] = ('#' if abs(cycles % 40 - x) <= 1 else ' ')
        cycles += 1
        if (cycles + 20) % 40 == 0: res += x * cycles
    elif command[0] == "addx":
        display[cycles // 40][cycles % 40] = ('#' if abs(cycles % 40 - x) <= 1 else ' ')
        cycles += 1
        if (cycles + 20) % 40 == 0: res += x * cycles
        display[cycles // 40][cycles % 40] = ('#' if abs(cycles % 40 - x) <= 1 else ' ')
        cycles += 1
        if (cycles + 20) % 40 == 0: res += x * cycles
        x += command[1]

[print(''.join(line)) for line in display]