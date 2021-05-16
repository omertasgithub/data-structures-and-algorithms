#716. Calculate Money in Leetcode Bank
#related topics
#Math, Greedy
n=4
n2=10
n3 = 20

#first solution
def totalMoney(n):
    num_monday = n//7
    remaining = n%7
    total = 0
    for i in range(num_monday):
        total+= 28 + 7*i
        
    total += sum(range(num_monday+1,remaining+num_monday+1))
    return total
print(totalMoney(n))
print(totalMoney(n2))
print(totalMoney(n3))


#second solution
def totalMoney2(n):
    weeks = n // 7
    remaining = n % 7
    total=0
    for i in range(weeks):
        total += 28  + 7*i
    total += remaining*(weeks+1 + remaining+weeks)/2
    return total

print(totalMoney2(n))
print(totalMoney2(n2))
print(totalMoney2(n3))


#one line solution
def totalMoney3(n):
        return sum([i//7 + i%7 + 1 for i in range(n)])
    
print(totalMoney3(n))
print(totalMoney3(n2))
print(totalMoney3(n3))  
    