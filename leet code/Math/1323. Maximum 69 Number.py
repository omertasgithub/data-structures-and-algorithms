#1323. Maximum 69 Number
#related topics 
#math

num = 9669
num2 = 9996
num3 = 9999


#first solution

def maximum69Number(num):
    s = str(num)
    maximum = 0
    for i in range(len(s)):
        c1 = s[:i]+'9'+ s[(i+1):]
        
        maximum = max(int(c1),maximum)
    return maximum

print(maximum69Number(num))
print(maximum69Number(num2))
print(maximum69Number(num3))