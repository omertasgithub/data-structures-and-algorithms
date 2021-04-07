#1351. Count Negative Numbers in a Sorted Matrix
#Related topics
#array, binary search

grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
grid2 = [[3,2],[1,0]]
grid3 = [[1,-1],[-1,-1]]
grid4 = [[-1]]


#first solution
def countNegatives(grid):
    count = 0
    for i in grid:
        for j in i:
            if j<0:
                count+=1
                
    return count

print(countNegatives(grid))
print(countNegatives(grid2))
print(countNegatives(grid3))
print(countNegatives(grid4))



#second solution
def countNegatives2(grid):
    return sum(a<0 for i in grid for a in i)

print(countNegatives2(grid))
print(countNegatives2(grid2))
print(countNegatives2(grid3))
print(countNegatives2(grid4))



#binary search?
