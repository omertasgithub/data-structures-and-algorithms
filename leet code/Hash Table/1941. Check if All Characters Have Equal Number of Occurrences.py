#1941. Check if All Characters Have Equal Number of Occurrences
#related topics
#hash table,couting


s = "abacbc"
s = "aaabb"

def areoccurrencesEqual(s):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    return len(set(dic.values()))==1     

print(areoccurrencesEqual(s))       

from collections import Counter
def areoccurrencesEqual(s):
    return len(set(Counter(s).values())) == 1
