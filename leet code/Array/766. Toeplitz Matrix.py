#766. Toeplitz Matrix
#related topics
#rray


matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]

matrix2 = [[1,2],[2,2]]

#first Solution
def isToeplitzMatrix(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            if matrix[i][j]!=matrix[i+1][j+1]:
                return False
    return True 

print(isToeplitzMatrix(matrix))
print(isToeplitzMatrix(matrix2))


#second solution
    def isToeplitzMatrix(self, m):
        return all(m[i][j] == m[i+1][j+1] for i in range(len(m)-1) for j in range(len(m[0])-1))
    
#third solutoin
def isToeplitzMatrix(self, m):
        return all(r1[:-1] == r2[1:] for r1,r2 in zip(m, m[1:]))     