import fractions
import time

start=time.time()

count=0
num=0
for i in xrange(1,1000+1):
    num=fractions.Fraction(1,2+num)
    st=str(1+num).split('/')
    if len(st[0])>len(st[1]):
        count+=1

print count
print time.time()-start

#153
#1.03399991989
