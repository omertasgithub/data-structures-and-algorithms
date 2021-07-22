#231. Power of Two
#realted topics 
#math, bit, recursion


def isPowerofTwo(n):
    return bin(n)[2:].count('1')==1 and n>0

print(isPowerofTwo(1))
print(isPowerofTwo(16))
print(isPowerofTwo(3))
print(isPowerofTwo(4))
print(isPowerofTwo(5))
print(isPowerofTwo(-16))
print("\n")
def isPowerofTwo(n):
    while n>=1:
        n=n/2
    return n==0.5

print(isPowerofTwo(1))
print(isPowerofTwo(16))
print(isPowerofTwo(3))
print(isPowerofTwo(4))
print(isPowerofTwo(5))
print(isPowerofTwo(-16))

