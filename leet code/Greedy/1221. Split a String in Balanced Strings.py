#1221. Split a String in Balanced Strings
#related topics
#string and greedy


s = 'RLRRLLRLRL'
s2 = "RLLLLRRRLR"
s3 = "LLLLRRRR"


#first solution

def balancedStringSplit(s):
    cnt = 0
    res = 0
    for i in s:
        if i=='L':
            cnt+=1
        else:
            cnt-=1
        if cnt==0:
            res+=1
    return res

print(balancedStringSplit(s))
print(balancedStringSplit(s2))
print(balancedStringSplit(s3))


#second solution
def balancedStringSplit2(s):
    res = cnt = 0         
    for c in s:
        cnt += 1 if c == 'L' else -1            
        if cnt == 0:
            res += 1
    return res  

print(balancedStringSplit2(s))
print(balancedStringSplit2(s2))
print(balancedStringSplit2(s3))

#third solution
from itertools import accumulate as acc
def balancedStringSplit3(s):
    return list(acc(1 if c=='L' else -1 for c in s)).count(0)


print(balancedStringSplit3(s))
print(balancedStringSplit3(s2))
print(balancedStringSplit3(s3))



