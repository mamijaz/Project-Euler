def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True

def Pro_Prime(limit):
    primes=[]
    if limit>=3:
        primes.append(2)
    for num in range(3,limit,2):
        if IsPrime(num):
            primes.append(num)
    return primes

def Totient_Ratio_Max(prime_range,limit):
    primes=Pro_Prime(prime_range)
    num=1
    for prime in primes:
        if num*prime>limit:
            return num
        num*=prime
    return 'Increase the prime range'

print Totient_Ratio_Max(100,10**6)
    
#510510

        
