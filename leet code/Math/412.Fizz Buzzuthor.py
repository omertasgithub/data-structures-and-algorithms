#412. Fizz Buzzuthor: omertas
#realted topics
#math, simulation

n=15

lst = [str(i) for i in range(1,n+1)]
for i,j in enumerate(lst):
    j=int(j)
    if j%3==0 and j%5==0:
        lst[i]="FizzBuzz"
    if j%3==0 and j%5!=0:
        lst[i]="Fizz"
    if j%3!=0 and j%5==0:
        lst[i]="Buzz"
    
print()
        

def fizzBuzz(self, n):
    return ['Fizz' * (not i % 3) + 'Buzz' * (not i % 5) or str(i) for i in range(1, n+1)]