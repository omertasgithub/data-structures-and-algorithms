#657. Robot Return to Origin
#related topics
#string

moves = "UD"
moves2 = "LL"
moves3 = "RRDD"
moves4 = "LDRRLRUULR"

#first solution
def judgeCircle(moves):
   
    u = moves.count("U")
    d = moves.count("D")
    r = moves.count("R")
    l = moves.count("L")
    return (abs(u-d)+abs(l-r))==0

print(judgeCircle(moves))
print(judgeCircle(moves2))
print(judgeCircle(moves3))
print(judgeCircle(moves4))


#second solution

def judgeCircle2(moves):
    return moves.count('L')==moves.count('R') and \
        moves.count('U') == moves.count('D')
        
print(judgeCircle2(moves))
print(judgeCircle2(moves2))
print(judgeCircle2(moves3))
print(judgeCircle2(moves4))


from collections import Counter
def judgeCircle3(moves):
    c=Counter(moves)
    return c['L']==c["R"] and c['U']==c['D']
