#744. Find Smallest Letter Greater Than Target
#binary search


letters1 = ["c","f","j"]
target1 = "a"
letters2 = ["c","f","j"]
target2 = "c"

letters3 = ["c","f","j"]
target3 = "g"
letters4 = ["c","f","j"]
target4 = "j"


#first solution
def nextGreatestLetter(letters, target):
    for i in letters:
        if ord(i)-ord(target) > 0:
            return i
            break
    return letters[0]

print(nextGreatestLetter(letters1, target1))
print(nextGreatestLetter(letters2, target2))
print(nextGreatestLetter(letters3, target3))
print(nextGreatestLetter(letters4, target4))

letters = ["c","f","j"]
target = "c"
print(nextGreatestLetter(letters, target))


#binary search
def nextGreatestLetter(letters, target):
    if target >= letters[-1]:
        return letters[0]
    
    low, high = 0, len(letters)-1
    while low<=high:
        mid = (low+high)//2
        if letters[mid]>target:
            low = mid + 1
        else:
            high = mid - 1
        return letters[low]
        
    
    
letters = ["c","f","j"]
target = "c"
print(nextGreatestLetter(letters, target))