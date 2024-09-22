#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create an arry
    min_c = [float('inf')] * (total + 1)
    min_c[0] = 0

    for coin in coins:
        for a in range(coin, total + 1):
            # the Updte
            min_c[a] = min(min_c[a], min_c[a - coin] + 1)

    # rreturn the min nber of coins
    return min_c[total] if min_c[total] != float('inf') else -1
