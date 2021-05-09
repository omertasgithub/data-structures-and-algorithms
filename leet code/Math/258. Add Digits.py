#258. Add Digits
#related topics 
#Math

num = 38
num2=0
num3=9
num4=10

#first solution   
def addDigits(num):
    if num<=9:
        return num
    while 9 < num:
        r = str(num)
        num = sum([int(i) for i in r])
    return num

print(addDigits(num))
print(addDigits(num2))
print(addDigits(num3))
print(addDigits(num4))

#divide by 9
def addDigits2(num):
    return 0 if num==0 else (num-1)%9+1

print(addDigits2(num))
print(addDigits2(num2))
print(addDigits2(num3))
print(addDigits2(num4))


#third solution
def addDigits3(num):
    while num>9:
        num=sum(int(c) for c in str(num))
    return num

print(addDigits3(num))
print(addDigits3(num2))
print(addDigits3(num3))
print(addDigits3(num4))
