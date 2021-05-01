#1491. Average Salary Excluding the Minimum and Maximum Salary
#related tpics
#string, sort


salary = [4000,3000,1000,2000]
salary2 = [1000,2000,3000]
salary3 = [6000,5000,4000,3000,2000,1000]

#first solution
def average(salary):
    salary.sort()
    salary = salary[1:-1]
    
    return sum(salary)/len(salary)
print(average(salary))
print(average(salary2))
print(average(salary3))


#second solution
def average2(salary):
    return float((sum(salary)-max(salary)-min(salary)))\
        /float((len(salary)-2))

print(average2(salary))
print(average2(salary2))
print(average2(salary3))