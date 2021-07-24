#202. Happy Number
#realted topcs
#hash table, math, two pointers


def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    seen = set()
    while n not in seen:
        seen.add(n)
        n=sum(i**2 for i in map(int,str(n)))
    return n==1
   
print(isHappy(19))
print(isHappy(2))