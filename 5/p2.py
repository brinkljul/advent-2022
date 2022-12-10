with open('input.txt', 'r') as f:
    # read the file
    lines = f.read()[:-1].split('\n\n')

# segment into stacks vs moves
lines = [segment.split('\n') for segment in lines]

boxes = lines[0]
moves = lines[1]

# get rid of the number listing under the boxes diagram
boxes = boxes[:-1]

# simplify moves section by removing commands and spaces
moves = [line.replace("move", "").replace("from", "").replace("to", "") for line in moves]
moves = [line.split(' ') for line in moves]
moves = [[int(move) for move in line if move != ''] for line in moves]

# get only the 2nd, 6th, 10th, etc... characters from the first segment
boxes = [line[1::4] for line in boxes]

# convert lines[0] to a 2d matrix
boxes = [list(line) for line in boxes]

# rotate lines[0] 90 degrees clockwise
boxes = [list(line) for line in zip(*boxes[::-1])]

# remove spaces from boxes
boxes = [[i for i in line if i != ' '] for line in boxes]

# subtract 1 from each element in the 2d moves array to get it to match 0-indexing
moves = [[move[0], move[1] - 1, move[2] - 1] for move in moves]

# awesome! now our data is finally nicely structured, we can start working on the problem
for move in moves:
    boxes[move[2]] = boxes[move[2]] + boxes[move[1]][-move[0]:]
    boxes[move[1]] = boxes[move[1]][:-move[0]]

# arrays look good! now i want a string composed of the last element of each stack
solution = ''.join([stack[-1] for stack in boxes])
print(solution)