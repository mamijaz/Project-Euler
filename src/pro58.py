import time

start=time.time()

def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True
    

digonalnumbers=['0'] #to have an extra element which a square,surely not a prime
diagonalprimes=[]
n=1
while True:
    for i in xrange(4):
        fn=n**2+i*(n+1)
        digonalnumbers.append(fn)
        if i:
            if IsPrime(fn):
                diagonalprimes.append(fn)
    if len(diagonalprimes)*1.0/len(set(digonalnumbers))<10.0/100:
        break
    n+=2
print n+2
print time.time()-start

#26241 60.0169999599
