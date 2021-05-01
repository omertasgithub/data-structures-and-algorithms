#1768. Merge Strings Alternately
#related topics
#string

#first solution
word1 = "abc"
word2 = "pqr"
word12 = "ab"
word22 = "pqrs"
word13 = "abcd"
word23 = "pq"
def mergeAlternately(word1,word2):
    l1 = len(word1)
    l2 = len(word2)
    res = []
    for i,j in zip(word1,word2):
        res+=[i,j]
    
    if l1-l2 > 0:
        res+=word1[l2:l1]
    else:
        res+=word2[l1:l2]
    return "".join(res)

print(mergeAlternately(word1, word2))
print(mergeAlternately(word12, word22))
print(mergeAlternately(word13, word23))


#Second solution
from itertools import zip_longest
def mergeAlternately2(word1,word2):
    return ''.join(i+j for i,j \
                   in zip_longest(word1,word2,fillvalue=''))
        


print(mergeAlternately2(word1, word2))
print(mergeAlternately2(word12, word22))
print(mergeAlternately2(word13, word23))



#third solution
def mergeAlternately3(word1,word2):
    res=''
    for i in range(min(len(word1),len(word2))):
        res+=word1[i]+word2[i]
    return res + word1[i+1:] + word2[i+1:]


print(mergeAlternately3(word1, word2))
print(mergeAlternately3(word12, word22))
print(mergeAlternately3(word13, word23))

    