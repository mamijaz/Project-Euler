def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True

primes=[]

for i in range(1,1000):
    if IsPrime(i):
        primes.append(i)

        
target = 1000
ways = [1] + [0]*target

for prime in primes:
    for i in range(prime, target+1):
        ways[i] += ways[i-prime]

for i in ways:
    if i>5000:
        print ways.index(i)
        break

#71
