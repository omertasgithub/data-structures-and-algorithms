#242. Valid Anagram
#related topics
#hash table, sorting

s = "anagram"
t = "nagaram"

def isAnagram(s,t):
    return sorted(list(s))==sorted(list(s))

#second solution

#wrong
def isAnagram(s,t):
    dic = {}

    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    for i in t:
        if i in dic:
            dic[i]-=1
    
    return set(dic.values())=={0}

print(isAnagram(s, t))
            
def isAnagram1(self, s, t):
    return collections.Counter(s) == collections.Counter(t)
