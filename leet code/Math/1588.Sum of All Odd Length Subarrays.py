#263. Ugly Number
#realted topics
#math

n=[6,8,14,1]

#first solution
#did not work Time limit Exceeded
#because 0 puts it in infinityloop
def isUgly(n):
    if n<=0:
        return False
    
    while True:
        if n%2==0:
            n=n/2
        if n%3==0:
            n=n/3
        if n%5==0:
            n=n/5
        if any([n%2==0,n%3==0,n%5==0]):
            continue
        else:
            break
    return n==1
    
    
for i in n:
    print(isUgly(i))
    
    

#a==b<c    a==b and b<c
    
def isUgly2(n):
    for p in [2,3,5]:
        while n %p ==0  and 0<n:
            n= n/p
    return n==1

for i in n:
    print(isUgly2(i))