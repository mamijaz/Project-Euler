import time
d=10000
frac=[]

start=time.time()

for den in xrange(1,d+1):
    for neu in xrange(1,den):
        frac.append(float(neu)/den)

frac=set(frac)
print len(frac)
print time.time()-start

