#1700. Number of Students Unable to Eat Lunch
#stack, queue

students1 = [1,1,0,0]
sandwiches1 = [0,1,0,1]
students2 = [1,1,1,0,0,1]
sandwiches2 = [1,0,0,0,1,1]

def countStudents(students, sandwiches):
    while sandwiches:
        if sandwiches[0] in students:
            students.remove(sandwiches[0])
            sandwiches.pop(0)
        else:break
    return len(students)

print(countStudents(students1, sandwiches1))
print(countStudents(students2, sandwiches2))
print("\n")

def countStudents(students, sandwiches):
    try:
        for s in sandwiches:
            students.remove(sandwiches)
    except:
        pass
    return len(students)


print(countStudents(students1, sandwiches1))
print(countStudents(students2, sandwiches2))



def countStudents(students, sandwiches):
    from collections import Counter

    students = Counter(students)
    for s in sandwiches:
        if not students[s]:
            break
        students[s]-=1
    return sum(students.values())

print(countStudents(students1, sandwiches1))
print(countStudents(students2, sandwiches2))




