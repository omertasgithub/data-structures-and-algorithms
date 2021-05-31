#1450. Number of Students Doing Homework at a Given Time
#realted topics
#array
startTime = [1,2,3]
endTime = [3,2,7]
queryTime = 4
num=0
for i,j in zip(startTime, endTime):
    if i<=queryTime and queryTime<=j:
        num+=1
        
    