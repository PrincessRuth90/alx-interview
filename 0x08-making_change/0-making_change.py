#!/usr/bin/python3
"""An n x n 2D matrix,rotate it 90 degrees clockwise"""


def makeChange(coins, total):
    """A pile of coins of different values"""
    if total <= 0:
        return 0

    current_total = 0
    coin_used = 0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        r = (total-current_total)//coin
        current_total += r*coin
        coin_used += r
        if current_total == total:
            return coin_used
    return -1
