# open the file

with open("input.txt", "r") as f:
    opp, me = [], []

    for line in f.read()[:-1].replace(" ", "").split('\n'):
        opp.append(line[0])
        me.append(line[1])

def value_rps_game(a, b):
    # second player loses
    if (a == "A" and b == "Z") or (a == "C" and b == "Y") or (a == "B" and b == "X"):
        return 0
    # draw
    elif ord(b) - ord(a) == 23:
        return 3
    # second player wins
    return 6

def value_used_item(b):
    # Rock worth 1, Paper worth 2, Scissors worth 3
    if b == "X":
        return 1
    elif b == "Y":
        return 2
    return 3

# sum value_rps_game and value_used_item(b) for each round
print(sum(value_rps_game(a, b) + value_used_item(b) for a, b in zip(opp, me)))