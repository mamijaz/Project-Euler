trinum=0
n=500
i=1
import time
t=time.time()

def numfactors(num):
    list1=[]
    for i in xrange(1,int(num**0.5)+1):
        if not num%i:
            list1.append(i)
            if list1[-1]!=num/i:
                list1.append(num/i)
    return len(list1)

while True:
    trinum=(i*(i+1))/2
    if numfactors(trinum)>=n:
        print trinum,i
        break
    i+=1
print (time.time()-t)
