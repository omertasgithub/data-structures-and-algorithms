#476. Number Complement
#related topics
#bit manupilation


num = 5
num2=1

#first solution
def findComplement(num):
    bin_num = list(bin(num)[2:])
    
    for i,n in enumerate(bin_num):
        if n=='1':
            bin_num[i]='0'
        else:
            bin_num[i]='1'
    x=''.join(['0b']+bin_num)
    return int(x,2)

print(findComplement(num))
print(findComplement(num2))


#second solution
def findComplement2(num):
    return num^(2**(len(bin(num)[2:]))-1)

print(findComplement2(num))
print(findComplement2(num2))