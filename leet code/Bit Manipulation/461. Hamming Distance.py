#461. Hamming Distance
#related topics
#bit manipulation

x=1
y=4
x1=3
y1=1


#first solution
def hammingDistance(x,y):
    x_bit = bin(x)[2:]
    y_bit = bin(y)[2:]
    
    if x>y:
        y_bit= (len(x_bit)-len(y_bit))*'0'+y_bit
    else:
        x_bit= (len(y_bit)-len(x_bit))*'0'+x_bit
    dif = 0    
    for i,j in zip(x_bit, y_bit):
        dif+=abs(int(i)-int(j))
    return dif

print(hammingDistance(x, y))
print(hammingDistance(x1, y1))

