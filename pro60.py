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
for i in xrange(3,10000,2):
    if IsPrime(i):
        primes.append(i)
def Five_Primes():
    for i in primes:
        for j in primes:
            if not IsPrime(int(str(i)+str(j))) or not IsPrime(int(str(j)+str(i))):continue
            for k in primes:
                if not IsPrime(int(str(k)+str(i))) or not IsPrime(int(str(i)+str(k))):continue
                if not IsPrime(int(str(k)+str(j))) or not IsPrime(int(str(j)+str(k))):continue
                for l in primes:
                    if not IsPrime(int(str(l)+str(i))) or not IsPrime(int(str(i)+str(l))):continue
                    if not IsPrime(int(str(l)+str(j))) or not IsPrime(int(str(j)+str(l))):continue
                    if not IsPrime(int(str(l)+str(k))) or not IsPrime(int(str(k)+str(l))):continue
                    for m in primes:
                        if not IsPrime(int(str(m)+str(i))) or not IsPrime(int(str(i)+str(m))):continue
                        if not IsPrime(int(str(m)+str(j))) or not IsPrime(int(str(j)+str(m))):continue
                        if not IsPrime(int(str(m)+str(k))) or not IsPrime(int(str(k)+str(m))):continue
                        if not IsPrime(int(str(m)+str(l))) or not IsPrime(int(str(l)+str(m))):continue
                        print i,j,k,l,m
                        print i+j+k+l+m
                        print time.time()-start
                        return
                    
Five_Primes()
#26033
#206.038000107
