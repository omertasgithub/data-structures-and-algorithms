#1539. Kth Missing Positive Number
#binary seearch
arr1 = [2,3,4,7,11]
k1 = 5

arr2 = [1,2,3,4]
k2 = 2

#first solution    
def findKthPositive(arr,k):
        i=1
        j=0
    
        while True:
           if i not in arr:
               j+=1
           if j==k:
               return i
           i+=1
    
print(findKthPositive(arr1, k1))
print(findKthPositive(arr2, k2))