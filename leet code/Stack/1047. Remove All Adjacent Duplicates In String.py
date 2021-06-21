#1047. Remove All Adjacent Duplicates In String
#realted topics
#stacks

s1 = "abbaca"
s2 = "azxxzy"

def removeDuplicates(s):
    stack = []
    for i in s:
        if stack and stack[-1]==i:
            stack.pop()
        else:
            stack.append(i)
    return "".join(stack)

print(removeDuplicates(s1))
print(removeDuplicates(s2))