#344. Reverse String
#related topics
#two pointers, string

#do not return anything
#must be in palce sort, reverse



#first solution
s = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]
def reverseString(s):
    s.reverse()
    
reverseString(s)
reverseString(s2)


#second solution
def reverseString2(s):
    s[:]=s[::-1] #not s=s[::-1]


