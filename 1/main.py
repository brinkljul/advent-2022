# advent of code day 1

# read the input file
with open("input.txt", "r") as f:
    # stop 1 before the end because the file has a trailing space
    lines = f.read()[:-1].split('\n\n')
    # split each line into a list of numbers
    lines = [list(map(int, line.split('\n'))) for line in lines]

# find the 3 lines with the biggest sum
lines.sort(key=lambda x: sum(x), reverse=True)

# print the sum of the first 3 lines
print(sum((sum(lines[0]), sum(lines[1]), sum(lines[2]))))