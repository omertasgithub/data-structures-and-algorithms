#205. Isomorphic Strings
#hash table, string

s = "egg"
t = "add"
s = "foo"
t = "bar"
s = "paper"
t = "title"

def isIsomorphic(s,t):
    dic = {}
    for i,n in enumerate(s):
        if n not in dic:
            dic[n]=t[i]
    if len(dic)!=len(set(dic.values())):
        return False         
            
    for i,j in zip(t,s):
        if dic[i]!=j:
            return False 
    return True 
