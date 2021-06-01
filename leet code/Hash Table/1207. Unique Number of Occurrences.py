#1207. Unique Number of Occurrences
#related topics
#hash table

arr = [1,2,2,1,1,3]
arr2 = [1,2]
arr3 = [-3,0,1,-3,1,1,1,-3,10,0]

#first solution
def uniqueOccurrences(arr):
    dic = {}
    for i in arr:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
            
    return len(dic.values())==len(set(dic.values()))


print(uniqueOccurrences(arr))
print(uniqueOccurrences(arr2))
print(uniqueOccurrences(arr3))