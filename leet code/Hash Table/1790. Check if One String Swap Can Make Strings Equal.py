#1790. Check if One String Swap Can Make Strings Equal
#related topics 
#hash table


s1 = "bank"
s2 = "kanb"

def areAlmostEqual(s1,s2):
    
    if len(s1)==1 and s1!=s2:
        return False 
    if len(s1)==2 and (s1!=s2 or s1!=s2[::-1]):
        return False
    s=0
    
    for i,j in zip(s1,s2):
        if i!=j:
            s+=1
    return s < 3 and sorted(s1)==sorted(s2)

print(areAlmostEqual(s1, s2))

diff = [[x, y] for x, y in zip(s1, s2) if x != y]


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff = [[x, y] for x, y in zip(s1, s2) if x != y]
        return not diff or len(diff) == 2 and diff[0][::-1] == diff[1]
    
    
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
		return s1 == s2 or sorted(s1) == sorted(s2) and sum(a != b for a, b in zip(s1, s2)) == 2