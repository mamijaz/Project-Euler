import time
start=time.time()

n=408393 #only two such apeare,num should be less than or eqal to sum of all facs from 1 to 9
digit_factorial=[]

def Factorial(num):
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)

for i in xrange(3,n):
    facsum=0
    for j in str(i):
        facsum+=Factorial(int(j))
    if i==facsum:
        digit_factorial.append(i)

print sum(digit_factorial)
print time.time()-start
