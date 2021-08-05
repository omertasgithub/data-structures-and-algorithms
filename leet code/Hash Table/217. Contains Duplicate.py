#217. Contains Duplicate
#array, hashtable, sorting


nums = [1,2,3,1]

def countainDuplicates(nums):
    if len(nums)==1:
        return False 
    dic = {}
    for i in nums:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
            
    if max(dic.values())>1:
        return False
    else:
        return True 
        
print(countainDuplicates(nums))

#using set
def countainDuplicates(nums):
    return len(nums)!=len(set(nums))