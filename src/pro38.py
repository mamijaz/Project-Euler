import time
start=time.time()

num=0
n=100000
for i in xrange(1,10):
    for j in xrange(1,n):
        st=''
        for k in xrange(1,i):
            st+=str(j*k)
        count=1
        for k in range(1,10):
            if len(st)!=9:
                count=0
            elif str(k) not in st:
                count=0
        if count==1 and int(st)>num:
            num=int(st)
print num
print time.time()-start
