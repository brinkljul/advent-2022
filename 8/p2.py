with open("input.txt", "r") as f:
    lines = f.read().splitlines()
    lines = [[int(ch) for ch in line] for line in lines]

visibility = [[1 for col in range(len(lines[0]))] for row in range(len(lines))]

for _ in range(4):
    for r, row in enumerate(lines):
        for t, tree in enumerate(row):
            visibility_mult = 0
            for ot in range(t + 1, len(row)):
                visibility_mult += 1
                if lines[r][ot] >= tree:
                    break
            visibility[r][t] *= visibility_mult
            
    # rotate lines and visibility 90 degrees clockwise
    lines = list(zip(*lines[::-1]))
    lines = [list(row) for row in lines]
    visibility = list(zip(*visibility[::-1]))
    visibility = [list(row) for row in visibility]

max_visibility = max([max(row) for row in visibility])
print(max_visibility)