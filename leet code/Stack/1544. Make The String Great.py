#1544. Make The String Great
#realted topics
#string, stack

s = "leEeetcode"
s2 = "abBAcC"
s3 = "s"

#first solution
def makeGood(s):
    stack = []
    for c in s:
        if not stack:
            stack.append(c)
        elif stack[-1].upper()==c.upper() and ord(stack[-1])!=ord(c):
            stack.pop()
        else:
            stack.append(c)
    return "".join(stack)

print(makeGood(s))
print(makeGood(s2))
print(makeGood(s3))

#second solution
def makeGood2(s):
    result = []
    for c in s:
        if not result:
            result.append(c)
        elif result[-1].isupper() and result[-1].lower() == c:
            result.pop()
        elif result[-1].islower() and result[-1].upper() == c:
            result.pop()
        else:
            result.append(c)
    return ''.join(result)

print(makeGood2(s))
print(makeGood2(s2))
print(makeGood2(s3))


#third solution
def makeGood3(s):
    stack = []        
    for c in s:
        if stack and stack[-1] == c.swapcase():
            stack.pop()
        else:
            stack.append(c)
            
    return "".join(stack)
print(makeGood3(s))
print(makeGood3(s2))
print(makeGood3(s3))
