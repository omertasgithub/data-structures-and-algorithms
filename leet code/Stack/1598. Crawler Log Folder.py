#1598. Crawler Log Folder
#related topics
#stack


logs1 = ["d1/","d2/","../","d21/","./"]
logs2 = ["d1/","d2/","./","d3/","../","d31/"]
logs3 = ["d1/","../","../","../"]


def minOperations(logs):
    stack = []

    for i in logs:
        if stack and i == "../":
            stack.pop()
        elif i == "./":
            pass
        else:
            if i!="../":
                stack.append(i)

            
    return len(stack)

print(minOperations(logs1))
print(minOperations(logs2))
print(minOperations(logs3))


def minOperations(logs):
    depth = 0
    for i in logs:
        if i == "../":
            depth = max(0, depth-1)
        elif i != "./":
            depth+=1
    return depth
print(minOperations(logs1))
print(minOperations(logs2))
print(minOperations(logs3))
