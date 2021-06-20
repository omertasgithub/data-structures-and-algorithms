#1684. Count the Number of Consistent Strings
#related topics 
#strings

allowed1 = "ab"
words1 = ["ad","bd","aaab","baa","badab"]
allowed2 = "abc"
words2 = ["a","b","c","ab","ac","bc","abc"]

allowed3 = "cad"
words3 = ["cc","acd","b","ba","bac","bad","ac","d"]

#first solutoin

def countConsistentStrings(allowed, words):
    total = []
    for i in words:
        lenght = len(i)
        r=0
        for j in i:
            if j in allowed:
                r+=1
        total.append(r==lenght)
        
    return sum(total)

print(countConsistentStrings(allowed1, words1))
print(countConsistentStrings(allowed2, words2))
print(countConsistentStrings(allowed3, words3))
print("\n")
#second solution
def countConsistentStrings(allowed, words):
    count= 0
    for i in words:
        if len(set(i).difference(set(allowed)))==0:
            count+=1
    return count

print(countConsistentStrings(allowed1, words1))
print(countConsistentStrings(allowed2, words2))
print(countConsistentStrings(allowed3, words3))

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        
        for word in words:
            for letter in word:
                if letter not in allowed:
                    count += 1
                    break
        
        return len(words) - count
