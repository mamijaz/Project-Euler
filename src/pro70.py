def Prime_Factors(num):
    prime_factor=[]
    while not num%2:
        prime_factor.append(2)
        num/=2
    primer=3
    while num!=1:
        while not num%primer:
            prime_factor.append(primer)
            num/=primer
        primer+=2
    return list(set(prime_factor))

def Totient_Function(num):
    totient=num
    primes_factors=Prime_Factors(num)
    for i in primes_factors:
        totient*=(i-1)
    for i in primes_factors:
        totient/=i
    return totient


def IsPermutation(num1,num2):
    count=1
    for i in str(num1):
        if str(num1).count(i)!=str(num2).count(i):
            count=0
            break
    if count:
        print num1,num2
        return True

            
min_ratio=1
min_n=1
limit=10**7

for num in xrange(2,limit):
    totient=Totient_Function(num)
    if IsPermutation(num,totient):
        if (float(num)/totient)<min_ratio:
            min_ratio=float(num)/totient
            min_n=num
    
print  min_n
