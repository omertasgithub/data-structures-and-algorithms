#338. Counting Bits
#related topics
#dynamic prograaming, bit manupilation


n=2
n2=5

#first solution
def countBits(n):
    res = []
    for i in range(n+1):
        res.append(sum(list(map(int,bin(i)[2:]))))
    return res

print(countBits(n))
print(countBits(n2))


n=2
n2=5
lst =[]
#second solution
for i in range(n+1):
    lst.append(bin(i)[2:])
    
for i in range(len(lst)):
    c = lst[i].count('0')
    
    lst[i]=len(lst[i])-c
    
    
#third solution
n=2
n2=5
lst =[]
for i in range(n+1):
    lst.append(bin(i)[2:])
    
for i in range(len(lst)):
    c = lst[i].replace('0','')
    
    lst[i]=len(c)
    
    
#dynamic programing
#work on later



   
    
    