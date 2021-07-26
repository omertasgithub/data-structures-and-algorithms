#389. Find the Difference
#realted topics
#hash table, string, bit manipulation, sorting

s = "abcd"
t = "abcde"


#first solution
def findTheDifference(s,t):
    return chr(sum(map(ord, list(t)))-sum(map(ord,list(s))))


def findTheDifference(s,t):
    dic = {}

    for i in t:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
            
    for i in s:
        dic[i]-=1
    
        
    return "".join([k for k, v in dic.items() if v==1])

print(findTheDifference(s,t))


def findTheDifference(s,t):
    concat = s+t
    dic = {}
    for i in concat:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
            
    for k,v in dic.items():
        if v%2!=0:
            return k