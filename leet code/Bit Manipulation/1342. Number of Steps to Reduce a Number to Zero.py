#1342. Number of Steps to Reduce a Number to Zero
#related topics
#bit manioulation


num = 14
num1 = 8
num2=123
        
        
def numberOfSteps(num):
     
     steps=0
     while 1<=num:
         if num%2==0:
             num = num/2
             steps+=1
         if num%2!=0:
             num=num-1
             steps+=1
     
     return steps


print(numberOfSteps(num))
print(numberOfSteps(num1))
print(numberOfSteps(num2))



def numberOfSteps (num):
        return bin(num).count("1") * 2 + bin(num).count("0") - 2
    
    
    
def numberOfSteps(num):
        bitstring = bin(num)[2:] # [2:] will remove the '0b' that is prepended to each bitstring by bin()
        return len(bitstring) - 1 + bitstring.count('1')
