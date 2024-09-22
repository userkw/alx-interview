#!/usr/bin/python3

""" makeChange function """

def makeChange(coins, total):
    """
    Calculates minimum coins needed for a total.
    Returns: coin count or -1 if impossible.
    """
    if not coins or coins is None:
        return -1
    if total <= 0:
        return 0
    var = 0
    coins = sorted(coins)[::-1]
    for coin in coins:
        while coin <= total:
            total -= coin
            var += 1
        if (total == 0):
            return var
    return -1
