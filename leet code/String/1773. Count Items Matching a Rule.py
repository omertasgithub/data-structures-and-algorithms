#1773. Count Items Matching a Rule
#related topics
#array, string
items = [["phone","blue","pixel"],
         ["computer","silver","phone"],
         ["phone","gold","iphone"]]

ruleKey = 'color'
ruleValue = 'silver'

items2 = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey2= "type"
ruleValue2 = "phone"

#first solution
def countMatches(items, ruleKey, ruleValue):
    dic = {'type':0,'color':1, 'name':2}
    position=dic[ruleKey]
    
    count=0
    for i in items:
        if ruleValue==i[position]:
            count+=1
    return count

print(countMatches(items, ruleKey, ruleValue))
print(countMatches(items2, ruleKey2, ruleValue2))



def countMatches2(items, ruleKey, ruleValue):
    dic = {'type':0,'color':1, 'name':2}
    position=dic[ruleKey]
    column = [col[position] for col in items]
    return sum([ruleValue==i for i in column])


print(countMatches2(items, ruleKey, ruleValue))
print(countMatches2(items2, ruleKey2, ruleValue2))