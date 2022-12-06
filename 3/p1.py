with open('input.txt', 'r') as f:
    lines = f.read().splitlines()
    # for each line, split it in the middle and save both halves to a tuple
    lines = [(line[:(len(line)//2)], line[(len(line)//2):]) for line in lines]
    
    matches = []
    for line in lines:
        # for each tuple, find a character in the first half that matches a character in the second half, then save it to matches
        for char in line[0]:
            if char in line[1]:
                matches.append(char)
                break
    
def letter_value(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

def sum_list_values(input_list):
    return sum([letter_value(char) for char in input_list])

print(sum_list_values(matches))