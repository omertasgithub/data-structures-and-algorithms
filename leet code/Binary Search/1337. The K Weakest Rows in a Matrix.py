#1337. The K Weakest Rows in a Matrix
#related topics
#binary search, array


mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k=3

mat2 = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k2= 2


#first solution
def KWeakestRows(mat, k):
    dic = {}

    for i,n in enumerate(mat):
        dic[i] = sum(n)
    
    dic_ord = sorted(dic.items(), key=lambda x:(x[1],x[0]))
    
    return [i[0] for i in dic_ord[:k]]


print(KWeakestRows(mat, k))
print(KWeakestRows(mat2, k2))

#binary search


