# use context manager to read the file
with open('input.txt', 'r') as f:
    # read the file
    line = f.read()

def check_uniques(substr):
    if len(set(substr)) == len(substr):
        return True
    return False

def find_uniques(line, length):
    for i in range(len(line)):
        current_substr = line[i:i+length]
        if check_uniques(current_substr):
            return i + length

print(find_uniques(line, 4))
print(find_uniques(line, 14))