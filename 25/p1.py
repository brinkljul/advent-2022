with open("input.txt", "r") as f:
    lines = f.read().splitlines()

d_snafu_dec = {"2": 2, "1": 1, "0": 0, "-": -1, "=": -2}
d_dec_snafu = {4: "2", 3: "1", 2: "0", 1: "-", 0: "="}

def snafu_to_dec(in_):
    out_ = 0
    for exponent, character in enumerate(in_[::-1]):
        multiplier = 5**exponent
        out_ += d_snafu_dec[character] * multiplier
    return out_

def dec_to_snafu(in_):
    out_ = ""
    while in_ > 0:
        in_, pos = divmod(in_ + 2, 5)
        out_ += d_dec_snafu[pos]
    return out_[::-1]

sum_ = sum(list(map(snafu_to_dec, lines)))
print(dec_to_snafu(sum_))