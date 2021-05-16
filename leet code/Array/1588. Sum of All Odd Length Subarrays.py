#1588. Sum of All Odd Length Subarrays
#related topics
#array

arr = [1,4,2,5,3]
arr2 = [1,2]
arr3 = [10,11,12]

            
#first solution
def sumOddLengthSubarrays(arr):
    s=0
    for i in range(1,len(arr)+1,2):
        lsts=[arr[j:j+i] for j in range(len(arr))]
        for lst in lsts:
            if len(lst)>=i:
                s+=sum(lst)
    return s

print(sumOddLengthSubarrays(arr))
print(sumOddLengthSubarrays(arr2))
print(sumOddLengthSubarrays(arr3))


#secod solution

#first solution
def sumOddLengthSubarrays2(arr):
    s=sum(arr)
    for i in range(3,len(arr)+1,2):
        lsts=[sum(arr[j:j+i]) for j in range(len(arr)-(i-1))]
        s+= sum(lsts)
    return s

print(sumOddLengthSubarrays2(arr))
print(sumOddLengthSubarrays2(arr2))
print(sumOddLengthSubarrays2(arr3))


res, n = 0, len(arr)
for i, a in enumerate(arr):
    res+=((i+1)*(n-i)+1)/2*a
    print(res)
    

#check later

def sumOddLengthSubarrays(self, A):
    res, n = 0, len(A)
    for i, a in enumerate(A):
        res += ((i + 1) * (n - i) + 1) / 2 * a
    return res

def sumOddLengthSubarrays(self, A):
    return sum(((i + 1) * (len(A) - i) + 1) / 2 * a for i, a in enumerate(A))
