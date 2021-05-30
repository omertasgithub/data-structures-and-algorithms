#387. First Unique Character in a String
#related tpics
#hash table, string

s = "loveleetcode"
#fisrt solution

def firstUniqChar(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            return i
            break
    return -1

print(firstUniqChar(s))

#second solution

def firstUniqChar2(s):
    dic = {}
    #collection counters make free dic by the way
    
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for i,n in enumerate(dic.values()):
        if n==1:
            return i
            break
    return -1

print(firstUniqChar2(s))


letters='abcdefghijklmnopqrstuvwxyz'
index=[s.index(l) for l in letters if s.count(l) == 1]
