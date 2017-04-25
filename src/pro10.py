import time
start=time.time()
def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num:
        return True
num=2000000  
primesum=2
i=3
while i<num:
    if num%3:
        if IsPrime(i):
            primesum=primesum+i
    i=i+2


eplesed=time.time()-start
print primesum,eplesed
