#!/usr/bin/python3


def makeChange(coins, total):
    
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    rem = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            rem += 1
        if (total == 0):
            return rem
    return -1
