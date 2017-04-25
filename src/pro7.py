def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num!=1:
        return True

num=10001   
prime=2
primeCount=1
i=3
while primeCount!=num:
    if IsPrime(i):
        primeCount=primeCount+1
        if primeCount==num:print i
    i=i+2

