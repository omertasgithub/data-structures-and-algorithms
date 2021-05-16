#1678. Goal Parser Interpretation
#related topics
#string
command = "G()(al)"
command2 = "G()()()()(al)"
command3 = "(al)G(al)()()G"

#first solution
def interpret(command):
    return command.replace('()','o').replace('(al)', 'al')

print(interpret(command))
print(interpret(command2))
print(interpret(command3))


#second solution
#regex
import re

def interpret2(command):
    return re.sub('\(\)','o', re.sub('\(al\)','al',command))

print(interpret2(command))
print(interpret2(command2))
print(interpret2(command3))


#use dictionary
def interpret(command):
        d = {"(al)":"al", "()":"o","G":"G"}
        tmp= ""
        res=""
        for i in range(len(command)):
            tmp+=command[i]
            if(tmp in d):
                res+=d[tmp]
                tmp=""
        return res

