#844. Backspace String Compare
#related topics
#two pointers, string, stack, simulation




s1 = "ab#c"
t1 = "ad#c"
s2 = "ab##"
t2 = "c#d#"
s3 = "a##c"
t3 = "#a#c"
s4 = "a#c"
t4 = "b"
s5 = "xywrrmp"
t5= "xywrrmu#p"
s6 = "y#fo##f"
t6= "y#f#o##f"
def backspaceCompare(s,t):
    stack_s = []
    stack_t = []
    for i in s:
        if not stack_s or i !="#":
            stack_s.append(i)
        else:
            stack_s.pop()
    for j in t:
        if not stack_t or j !="#":
            stack_t.append(j)
        else:
            stack_t.pop()
    return stack_s == stack_t

print(backspaceCompare(s1, t1))
print(backspaceCompare(s2, t2))
print(backspaceCompare(s3, t3))
print(backspaceCompare(s4, t4))
print(backspaceCompare(s5, t5))

def backspaceCompare(s,t):
    stack_s = []
    stack_t = []
    for i in s:
        if stack_s and i =="#":
            stack_s.pop()
        else:
            stack_s.append(i)
    for j in t:
        if stack_t and j =="#":
            stack_t.pop()
        else:
            stack_t.append(j)
    stack_s = [i for i in stack_s if i!="#"]
    stack_t = [i for i in stack_t if i!="#"]
    return stack_s == stack_t

print(backspaceCompare(s1, t1))
print(backspaceCompare(s2, t2))
print(backspaceCompare(s3, t3))
print(backspaceCompare(s4, t4))
print(backspaceCompare(s5, t5))
print(backspaceCompare(s6, t6))


   
