#1528. Shuffle String

#related topics sort


s = 'codeleet'
indices = [4,5,6,7,0,2,1,3]

s1 = 'abc'
indices1 = [0,1,2]

#first solution
def restoreString(s,indices):
    dic = {}

    for i in range(len(s)):
         dic[indices[i]] = s[i]
    
    lst = []
    for i in sorted(dic):
        lst.append(dic[i])
    
    return "".join(lst)


print(restoreString(s, indices))
print(restoreString(s1, indices1))

#second solution

def restoreString2(s, indices):
    res = [''] * len(s)
    
    for index, char in enumerate(s):
        res[indices[index]] = char
    return "".join(res)

print(restoreString2(s, indices))
print(restoreString2(s1, indices1))
