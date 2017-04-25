n=1001
tot=1
for i in xrange(1,n/2+1):
    tot+=4*(2*i+1)**2-12*i
print tot
