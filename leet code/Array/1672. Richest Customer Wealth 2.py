


#related topics array
   


accounts = [[1,2,3],[3,2,1]] 
#first solutions
def maximumwealth(accounts):
    lst = []
    for i in accounts:
        lst.append(sum(i))
    return max(lst)
    

#map wow
    
def maximumwealth(accounts):
    return max(map(sum, accounts))

#list 
    
def maximumwealth(accounts):
    return max([sum(i) for i in accounts])