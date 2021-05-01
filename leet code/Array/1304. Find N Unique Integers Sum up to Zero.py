#1304. Find N Unique Integers Sum up to Zero
#related topics
#array



n = 6
n2=5
n3=3
n4=1

#first solution
def sumZero(n):
    if n==1:
        return [0]
    if n%2!=0:
        return list(range(-n//2+1,n//2+1))
    if n%2==0:
        lst = list(range(-n//2,n//2))
        lst[n-1]-=lst[0]
        return lst
        
print(sumZero(n))
print(sumZero(n2))
print(sumZero(n3))
print(sumZero(n4))


#second solution

#Naive idea
#n = 1, [0]
#n = 2, [-1, 1]

#Now write more based on this
#n = 3, [-2, 0, 2]
#n = 4, [-3, -1, 1, 3]
#n = 5, [-4, -2, 0, 2, 4]


def sumZero2(n):
    return range(1-n,n,2)


print(sumZero2(n))
print(sumZero2(n2))
print(sumZero2(n3))
print(sumZero2(n4))


#third solution
def sumZero(n):
    a = range(1, n)
    return a + [-sum(a)]

