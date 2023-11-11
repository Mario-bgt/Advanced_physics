import random

random.seed(7)


def lottery(limit, guess, prize):
    generated = random.sample(range(1, limit + 1), len(guess))
    right = 0
    for val in guess:
        if val in generated:
            right += 1
    if right == 0:
        payout = 0
    else:
        payout = prize / (2 ** (len(guess) - right))
    return sorted(generated), right, payout


print(lottery(52, [4, 8, 15, 16, 23, 42], 1000000))
print(lottery(3, [1, 2, 3], 1000000))
print(lottery(10000, [1, 2, 3], 1000000))
