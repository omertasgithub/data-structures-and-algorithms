#1051. Height Checker
#related topics
#array



heights = [1,1,4,2,1,3]
heights2 = [5,1,2,3,4]
heights3 = [1,2,3,4,5]
#first solution
r = 0
for i,j in zip(heights, sorted(heights)):
    if i!=j:
        r+=1

def heightChecker(heights):
    r = 0
    for i,j in zip(heights, sorted(heights)):
        if i!=j:
            r+=1
    return r

print(heightChecker(heights))
print(heightChecker(heights2))
print(heightChecker(heights3))


#Second solution
def heightChecker2(heights):
    return sum(1 if i!=j else 0 for i,j in zip(heights, sorted(heights)))

print(heightChecker2(heights))
print(heightChecker2(heights2))
print(heightChecker2(heights3))

#third solution
