

#1431. Kids With the Greatest Number of Candies
#realtes topics
#array

candies = [2,3,5,1,3]
extraCandies = 3
candies2 = [4,2,1,1,2]
extraCandies2 = 1
candies3 = [12,1,12]
extraCandies3 = 10

#first solution
def kidsWithCandies(candies, extraCandies):
    res = [None] * len(candies)
    for i,candy in enumerate(candies):
        result = max(candies) <= candy + extraCandies
        res[i]=result
    return res
        
print(kidsWithCandies(candies,extraCandies))
print(kidsWithCandies(candies2,extraCandies2))
print(kidsWithCandies(candies3,extraCandies3))

#Second solution
import numpy as np
def kidsWithCandies2(candies,extraCandies):
    return list(max(candies) <= np.array(candies) + extraCandies)


#third solution
def kidsWithCandies3(candies,extraCandies):
    high = max(candies) - extraCandies
    return [i >= high for i in candies]