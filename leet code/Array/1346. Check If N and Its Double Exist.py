
#1346. Check If N and Its Double Exist
#related topics
#array
arr = [10,2,5,3]
arr2 = [7,1,14,11]
arr3 = [3,1,7,11]

#first solution
def checkIfExist(arr):
    for i,n in enumerate(arr):
        if 2*n in arr[(i+1):]+arr[:-(len(arr)-i)]:
            return True
    return False 

print(checkIfExist(arr))
print(checkIfExist(arr2))
print(checkIfExist(arr3))

#look later
class Solution:
  def checkIfExist(self, arr: List[int]) -> bool:
    
    s = collections.Counter(arr)
    
    #check if there are more than one zeros
    if(s[0]>1): return True;
    
    
    for num in arr:
      if s[2*num] and num!=0:
        return True
    return False