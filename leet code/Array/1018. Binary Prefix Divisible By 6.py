#1018. Binary Prefix Divisible By 5
#reated topics
#Array

A = [0,1,1]
A2=[1,1,1]
A3 = [0,1,1,1,1,1]
A4 =  [1,1,1,0,1]


#first solution
def prefixesDivBy5(A):
    A=[str(i) for i in A]
    lst = []
    for i,n in enumerate(A):
        decimal = int(''.join(A[0:(i+1)]),2)
        if decimal%5==0:
            lst+= [True]
        else:
            lst += [False]
    return lst

print(prefixesDivBy5(A))
print(prefixesDivBy5(A2))
print(prefixesDivBy5(A3))
print(prefixesDivBy5(A4))

#check later

def prefixesDivBy5(self, A):
        for i in xrange(1, len(A)):
            A[i] += A[i - 1] * 2 % 5
        return [a % 5 == 0 for a in A]
    
    
def prefixesDivBy5(self, A):
        sums = 0
        for i, a in enumerate(A):
            sums = sums * 2 % 5 + a
            A[i] = sums % 5 == 0
        return A
    
def prefixesDivBy5(self, A):
        return [x % 5 == 0 for x in accumulate(A, lambda x, y: (x << 1) + y)]