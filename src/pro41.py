import time
start=time.time()
num=0

def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True
    
for i in xrange(11,10000000):
    st=str(i)
    count=1
    for j in xrange(1,len(st)+1):
        if str(j) not in st:
            count=0
            break
    if count==1 and IsPrime(i):
        num=i
print num
print time.time()-start
#7652413

