import time

start=time.time()

circular_prime_count=[]
n=1000000

def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num!=1:
        return True

for i in xrange(1,n):
    if IsPrime(i):
        a=[]
        st=str(i)
        for j in range(len(str(i))):
            st1=st[-1]
            st2=st[0:-1]
            st=st1+st2
            a.append(int(st))
        count=1
        for j in a:
            if not IsPrime(j):
                count=0
                break
        if count==1:
            circular_prime_count.append(i)
        

print circular_prime_count
print len(circular_prime_count)
print time.time()-start
        
