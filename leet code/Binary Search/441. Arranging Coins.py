#441. Arranging Coins
#Binary search, math

#brute 
def arrangeCoins(n):
    """
    :type n: int
    :rtype: int
    """
    i=0
    while True:
        if (i * (i+1))/2 > n:
            return i-1
            break
        i+=1
    return i
import math
def arrangeCoins(n):
    return int(((8 * n + 1)**0.5-1)/2)

