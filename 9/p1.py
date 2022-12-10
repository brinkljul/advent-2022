with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    lines = [line.split(' ') for line in lines]
    moves = [[line[0], int(line[1])] for line in lines]

def adjust_tail(head, tail):
    dx = abs(head[0] - tail[0])
    dy = abs(head[1] - tail[1])

    if dx <= 1 and dy <= 1:
        return tail
    elif dx >= 2 and dy >= 2:
        if tail[0] < head[0]:
            tail = (head[0] - 1, tail[1])
        else:
            tail = (head[0] + 1, tail[1])
        if tail[1] < head[1]:
            tail = (tail[0], head[1] - 1)
        else:
            tail = (tail[0], head[1] + 1)
        return tail
    elif dx >= 2:
        if tail[0] < head[0]:
            tail = (head[0] - 1, head[1])
        else:
            tail = (head[0] + 1, head[1])
        return tail
    # dy >= 2
    if tail[1] < head[1]:
        tail = (head[0], head[1] - 1)
    else:
        tail = (head[0], head[1] + 1)
    return tail

# (x, y)
head = (0, 0)
tail = (0, 0)
REDIRECT_X = {'L': -1, 'R': 1, 'U': 0, 'D': 0}
REDIRECT_Y = {'U': -1, 'D': 1, 'L': 0, 'R': 0}
visited = set([tail])

for move in moves:
    for _ in range(move[1]):
        head = (head[0] + REDIRECT_X[move[0]], head[1] + REDIRECT_Y[move[0]])
        tail = adjust_tail(head, tail)
        visited.add(tail)

print(len(visited))