#884. Uncommon Words from Two Sentences
#related topics
#hash table

A = "this apple is sweet"
B = "this apple is sour"
A2 = "apple apple"
B2 = "banana"
#first solution
def uncommonFromSentence(A,B):
    s =  (A+ " " + B).split(" ")

    dic = {}
    
    for i in s:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
    
        
    lst = []
    
    for i,j in dic.items():
        if j==1:
            lst.append(i)
    return lst

print(uncommonFromSentence(A, B))
print(uncommonFromSentence(A2, B2))

#second solution
def uncommonFromSentence2(A,B):
    s = A.split(" ") + B.split(" ")
    lst = []
    for i in s:
        if s.count(i)==1:
            lst.append(i)
    return lst

print(uncommonFromSentence2(A, B))
print(uncommonFromSentence2(A2, B2))

import collections
def uncommonFromSentences(self, A, B):
        c = collections.Counter((A + " " + B).split())
        return [w for w in c if c[w] == 1]


