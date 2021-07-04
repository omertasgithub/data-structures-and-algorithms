#1614. Maximum Nesting Depth of the Parentheses
#related topics
#stack



s = "(1+(2*3)+((8)/4))+1"
s = "(1)+((2))+(((3)))"
#s = "1+(2*3)/(2-1)"
s = "1"
def maxDepth(self, s):
    """
    :type s: str
    :rtype: int
    """
    r = 0
    t=0
    for i in s:

        if i == "(":
             r+=1
             t = max(r,t)
        elif i==")":
            r-=1
        else:
            pass
    return t

#stack
def maxDepth(self, s: str) -> int:
        # use a stack, keep track of max length of stack
        stack = []
        max_len = 0
        for ch in s:
            if ch == '(':
                stack.append(ch)
                max_len = max(max_len, len(stack))
            elif ch == ')':
                stack.pop()
        return max_len