import time
start=time.time()
numrange=1000000
colnum=0
colcount=0
for i in xrange(1,numrange):
    num=i
    count=0
    while num!=1:
            if not num%2:num=num/2
            else:num=3*num+1
            count+=1
    if count>colcount:
        colcount=count
        colnum=i
print colnum
print (time.time()-start)

#837799
#69.8359999657
