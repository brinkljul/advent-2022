with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    lines = [[int(ch) for ch in line] for line in lines]

visibility = [[0 for col in range(len(lines[0]))] for row in range(len(lines))]

for _ in range(4):
    for r, row in enumerate(lines):
        for i in range(len(row)):
            if i == 0 or row[i] > max(row[:i]):
                visibility[r][i] = 1
    # rotate lines and visibility 90 degrees clockwise
    lines = list(zip(*lines[::-1]))
    lines = [list(row) for row in lines]
    visibility = list(zip(*visibility[::-1]))
    visibility = [list(row) for row in visibility]

# get the sum of visibility
visibility_sum = sum([sum(row) for row in visibility])
print(visibility_sum)