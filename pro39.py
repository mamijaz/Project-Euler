import time

start=time.time()

p_for_max=0
no_sol=0

for p in xrange(12,1001,2):#p in always even for right angle triangle
    count=0
    for x in xrange(1,p):
        for y in xrange(1,int((p**2-x**2)**0.5)+1):
            a=(x**2+y**2)**0.5
            if x+y+a==p:
                count+=1
    if no_sol<count:
        no_sol=count
        p_for_max=p

print p_for_max,no_sol
print time.time()-start
