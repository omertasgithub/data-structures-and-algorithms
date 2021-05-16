#342. Power of Four
#reated topics
#bit manipulation

n=16
n1=5
n2=1
from math import log
def isPowerOfFour(n):
    return log(n,4)==int(log(n,4))

print(isPowerOfFour(n))
print(isPowerOfFour(n1))
print(isPowerOfFour(n2))