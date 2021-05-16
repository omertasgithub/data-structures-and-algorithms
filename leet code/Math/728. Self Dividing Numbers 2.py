
#728. Self Dividing Numbers
#related topics 
#math

#first solution
def selfDividingNumbers(left, right):
    lst = []
    for i in range(left, right + 1):
        if '0' not in str(i) and sum([i%int(k) for k in str(i)])==0:
            lst.append(i)
    return lst
        

print(selfDividingNumbers(1, 22))