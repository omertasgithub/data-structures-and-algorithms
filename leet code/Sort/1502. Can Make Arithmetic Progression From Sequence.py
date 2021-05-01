#1502. Can Make Arithmetic Progression From Sequence

#related topics
#array, sort


arr = [3,5,1]
arr2 = [1,2,4]

def canMakeArithmeticProgression(arr):
     arr.sort()
     return arr==[arr[0]+(n-1)*(arr[1]-arr[0]) for n in range(1,len(arr)+1)]
        
print(canMakeArithmeticProgression(arr))
print(canMakeArithmeticProgression(arr2))

