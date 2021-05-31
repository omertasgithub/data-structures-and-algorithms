#905. Sort Array By Parity

#realted topics
#array

nums = [3,1,2,4]

#first solution
def sortArrayByParity(nums):
    lst = []
    for i in nums:
        if i %2==0:
            lst+=[i]
            
    for i in nums:
        if i%2!=0:
            lst+=[i]
    return lst


print(sortArrayByParity(nums))


#second solution
#takes even longer
lst = []
for i in nums:
    if i%2==0:
        lst=[i]+lst
    else:
        lst.append(i)
    
    
