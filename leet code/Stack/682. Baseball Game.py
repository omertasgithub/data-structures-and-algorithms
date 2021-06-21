#682. Baseball Game
#realted topics
#stack


ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]
ops = ["1"]

#first solution
def calPoints(ops):
    stack = []
    for i,n in enumerate(ops):
       
           
       if n=="+":
           stack.append(sum([stack[-2]+stack[-1]]))
       elif n=="D":
           stack.append(2*stack[-1])
       elif n=="C":
           stack.pop()
       else:
           stack.append(int(n))
           
    return sum(stack)


       
