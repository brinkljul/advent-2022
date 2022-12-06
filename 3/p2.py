with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

    groups = []
    # save each group of 3 from lines into a tuple in groups
    for i in range(0, len(lines), 3):
        groups.append((lines[i], lines[i+1], lines[i+2]))
    
    badges = []
    for group in groups:
        # find the letter that the 3 lines have in common
        for char in group[0]:
            if char in group[1] and char in group[2]:
                badges.append(char)
                break

    
def letter_value(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

def sum_list_values(input_list):
    return sum([letter_value(char) for char in input_list])

print(sum_list_values(badges))