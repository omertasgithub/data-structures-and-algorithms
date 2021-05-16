#1281. Subtract the Product and Sum of Digits of an Integer
#Related topics
#Math


n = 234
n2= 4421

#first solution
def subtractProductAndSum(n):
    s=0
    p=1
    for i in str(n):
        s+=int(i)
        p*=int(i)
    return p-s

print(subtractProductAndSum(n))
print(subtractProductAndSum(n2))

#second solution

def subtractProductAndSum2(n):
    return eval('*'.join(str(n)))-eval('+'.join(str(n)))



print(subtractProductAndSum2(n))
print(subtractProductAndSum2(n2))
   