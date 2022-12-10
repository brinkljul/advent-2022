import collections

# open the file and read the lines
with open("input.txt", "r") as f:
    lines = f.readlines()
    lines = [line.replace("\n", "") for line in lines]

# initialize the path and the directories
path = []
directories = collections.defaultdict(int)

# loop through the lines
for line in lines:
    pieces = line.strip().split()

    # if the command is ls, skip it
    if pieces[1] == "ls":
        continue

    # if the command is cd, change the path
    elif pieces[1] == "cd":
        if pieces[2] == "..":
            path.pop()
        elif pieces[2] == "/":
            path.clear()
        else:
            path.append(pieces[2])
    
    # if it's not a command, add the size to the directories
    else:
        # try to convert the size to an int
        try:
            size = int(pieces[0])
            for i in range(len(path) + 1):
                directories['/'.join(path[:i])] += size
        # if it's not an int, skip it
        except:
            pass

# figure out the best directory
min_space = 70000000 - directories['']
min_space = 30000000 - min_space
best_choice_k = ''

for k, v in directories.items():
    if v > min_space and v < directories[best_choice_k]:
        best_choice_k = k

print(best_choice_k, directories[best_choice_k])