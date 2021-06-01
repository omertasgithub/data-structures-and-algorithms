#1688. Count of Matches in Tournament
#realted topics
#backtracking

n=7
n2=14

#solution 1
        
def numberOfMatches(n):
    """
    :type n: int
    :rtype: int
    """
    m=0
    while 1<n:
        if n%2==0:
            m+=n/2
            n=n/2
        else:
            m+= (n-1)/2
            n=(n-1)/2+1
    return int(m)

print(numberOfMatches(n))
print(numberOfMatches(n2))

#solution 2

def numberOfMatches(n):
        return n - 1