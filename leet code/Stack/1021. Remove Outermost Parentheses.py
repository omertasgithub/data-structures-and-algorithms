#1021. Remove Outermost Parentheses
#reated topics
#stack

#first solution
s1 = "(()())(())"
s2 = "(()())(())(()(()))"
s3= "()()"
def removeOuterParentheses(S):
    res = ''
    basket = ''
    stack = []
    for i in S:
        if i=='(':
            stack.append(i)
        else:
            stack.pop()
        basket+=i
        
        if not stack:
            res+=basket[1:-1]
            basket = ''
    return res

print(removeOuterParentheses(s1))
print(removeOuterParentheses(s2))
print(removeOuterParentheses(s3))

#second solution
def removeOuterParentheses(self, S):
        res, opened = [], 0
        for c in S:
            if c == '(' and opened > 0: res.append(c)
            if c == ')' and opened > 1: res.append(c)
            opened += 1 if c == '(' else -1
        return "".join(res)



    

        
                
