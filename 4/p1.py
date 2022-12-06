def detect_overlap(line):
    if line[0] <= line[2] and line[1] >= line[3]:
        return 1
    elif line[2] <= line[0] and line[3] >= line[1]:
        return 1
    return 0

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    lines = [tuple(map(int, line.replace(',', '-').split('-'))) for line in lines]
    
    print(sum([detect_overlap(line) for line in lines]))