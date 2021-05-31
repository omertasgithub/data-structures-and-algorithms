#1859. Sorting the Sentence
#realted topics
#String, sorting


s = "is2 sentence4 This1 a3"

s2 = "Myself2 Me1 I4 and3"


def sortSentence(s):
    """
    :type s: str
    :rtype: str
    """
    dic = {}
    for i in s.split(" "):
        dic[int(i[-1])]=i[:-1]
  
    lst = sorted(dic.items())


    return " ".join([i[1] for i in lst])


print(sortSentence(s))
print(sortSentence(s2))

s = "is2 sentence4 This1 a3"
t = [0]*len(s.split())
for i in s.split(" "):
    t[int(i[-1])-1] = i[:-1]    