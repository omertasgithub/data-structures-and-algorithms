#1518. Water Bottles
#related topics
#simulation


numBottles = 15
numExchange = 4

total = numBottles
while numExchange <= numBottles:
    
    #you coudl use divmod
    numBottles = numBottles // numExchange
    remainder = numBottles % numExchange
    total+=numBottles
    numBottles+=remainder



#geomtric serious

numBottles + (numBottles - 1)//(numExchange - 1)