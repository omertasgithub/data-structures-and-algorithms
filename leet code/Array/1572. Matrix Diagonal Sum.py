#1572. Matrix Diagonal Sum
#related topics
#array

mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]

mat2 = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]

mat3 = [[5]]

#first solution

def diagonalSum(mat):
    l=len(mat[0])
    s=0
    for i in range(l):
        s+=mat[i][-1-i]+mat[i][i]
        
    if l%2!=0:
        s-=mat[l//2][l//2]
    return s
                
print(diagonalSum(mat))
print(diagonalSum(mat2))
print(diagonalSum(mat3))