import time

start=time.time()

def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True

primes=[2]
n=3
while True:
    if IsPrime(n):
        primes.append(n)
    else:
        count=0
        for i in primes:
            for j in range(1,int((n**0.5))):
                if n==i+2*j**2:
                    count+=1
        if count==0:
            break
    n+=2
    
print n
print time.time()-start

#5777 19.6679999828
