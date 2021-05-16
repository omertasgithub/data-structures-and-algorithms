#1844. Replace All Digits with Characters
#related topics
#string


s = "a1c1e1"
s2 = "a1b2c3d4e"
#first solution
def replaceDigits(s):
    s = list(s)
    for i in range(1, len(s),2):
        shifted = chr(int(s[i]) + ord(s[i-1]))
        s[i]=shifted
    return "".join(s)
    


print(replaceDigits(s))
print(replaceDigits(s2))


#second solution
def replaceDigits2(s):
    a=''
    for i in range(1, len(s),2):
        shifted = chr(int(s[i]) + ord(s[i-1]))
        a+=s[i-1]+shifted
    return a if len(s)%2==0 else a+s[len(s)-1]

print(replaceDigits2(s))
print(replaceDigits2(s2))