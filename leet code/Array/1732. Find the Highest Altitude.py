#1732. Find the Highest Altitude

#related topics
#array
z = [44,32,-9,52,23,-50,50,33,-84,47,-14,84,36,-62,37,81,-36,-85,-39,67,-63,64,-47,95,91,-40,65,67,92,-28,97,100,81]
gain = [-5,1,5,0,-7]
gain2 = [-4,-3,-2,-1,4,3,2]
gain3 = z   
#first solution
def largestAltitude(gain):
    lst = [0]
    for i,n in enumerate(gain):
        current = sum(gain[0:(i+1)])
        lst.append(current)
    return max(lst)

print(largestAltitude(gain))
print(largestAltitude(gain2))
print(largestAltitude(gain3))

    
#second solution
def largestAltitude2(gain):
    current = 0
    maxim = 0
    for i,n in enumerate(gain):
        
        
        current = current + n
        if maxim < current:
            maxim = current
    return maxim


print(largestAltitude2(gain))
print(largestAltitude2(gain2))
print(largestAltitude2(gain3))



#third solution
from itertools import accumulate

def largestAltitude3(gain):
    return max([0]+list(accumulate(gain)))
    #or
    # return max(0, max(accumulate(gains)))
               

print(largestAltitude3(gain))
print(largestAltitude3(gain2))
print(largestAltitude3(gain3))

#4th solution

def largestAltitude4(gain):
    current = 0
    maxim = 0
    for i,n in enumerate(gain):
        current += n
        maxim = max(maxim,current)
    return maxim


print(largestAltitude4(gain))
print(largestAltitude4(gain2))
print(largestAltitude4(gain3))