
#771. Jewels and Stones
#related topics
#Hash table


jewels = "aA"
stones = "aAAbbbb"

jewels2 = "z" 
stones2 = "ZZ"
        
def numJewelsInStones(jewels, stones):
    
    r=0
    for i in stones:
        if i in jewels:
            r+=1
    return r


print(numJewelsInStones(jewels, stones))
print(numJewelsInStones(jewels2, stones2))


def numJewelsInStones2(jewels, stones):
    hash = {}
    for jewel in jewels:
      if jewel not in hash:
        hash[jewel] = True

    cnt = 0

    for stone in stones:
      if stone in hash:
        cnt += 1

    return cnt

print(numJewelsInStones2(jewels, stones))
print(numJewelsInStones2(jewels2, stones2))
