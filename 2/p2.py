# open the file

with open("input.txt", "r") as f:
    opp, me = [], []

    for line in f.read()[:-1].replace(" ", "").split('\n'):
        opp.append(line[0])
        me.append(line[1])

def value_rps_game(a, b):
    if b == "Z":
        return 6
    elif b == "X":
        return 0
    return 3

def value_used_item(a, b):
    # this time b represents whether the second player wins (Z), loses (X), or draws (Y).

    if b == "Z":
        if a == "A":
            return 2
        elif a == "B":
            return 3
        return 1
    elif b == "X":
        if a == "A":
            return 3
        elif a == "B":
            return 1
        return 2
    elif b == "Y":
        if a == "A":
            return 1
        elif a == "B":
            return 2
        return 3

# sum value_rps_game and value_used_item(b) for each round
print(sum(value_rps_game(a, b) + value_used_item(a, b) for a, b in zip(opp, me)))