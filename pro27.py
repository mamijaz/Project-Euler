import time

start=time.time()
def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True
    
a_b=[0,0]
count=0

for a in xrange(-1000+1,1000,1):
    for b in xrange(-1000+1,1000,1):
        n=0
        while True:
            if not IsPrime(n**2+a*n+b):break
            else:n+=1
        if count<n:
                count=n
                a_b[0]=a
                a_b[1]=b
print count,a_b,a_b[0]*a_b[1]
print time.time()-start
