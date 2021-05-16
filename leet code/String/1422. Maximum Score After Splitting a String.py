#1422. Maximum Score After Splitting a String
#related topics
#string
s = "011101"
s2 = "00111"
s3 = "1111"

#first soluition 
def maxScore(s):
    m=0
    for i in range(1,len(s)):
        r = s[0:(i)].count('0') + s[i:].count('1')
        m = max(r,m)
    return m
print(maxScore(s))
print(maxScore(s2))
print(maxScore(s3))