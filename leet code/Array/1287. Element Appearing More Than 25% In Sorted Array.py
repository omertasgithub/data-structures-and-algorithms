#1287. Element Appearing More Than 25% In Sorted Array
#related topics
#array


arr = [1,2,2,6,6,6,6,7,10]
arr=[1,1]

#first solution
def findSpecialInteger(arr):
    for i in arr:
        if arr.count(i) > len(arr) /4:
            return i
            break

print(findSpecialInteger(arr))


#hast table fster than previous
dic = {}

for i in arr:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
sorted(dic.items(), key=lambda x:x[1])[-1][0] 


#third and more
class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return collections.Counter(A).most_common(1)[0][0]
		

from statistics import mode

class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return mode(A)


class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return max(set(A), key = A.count)
		
		
class Solution:
    def findSpecialInteger(self, A: List[int]) -> int:
        return (lambda C: max(C.keys(), key = lambda x: C[x]))(collections.Counter(A))