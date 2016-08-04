import time

start=time.time()

num=1
t=6
while True:
    count=0
    for i in str(num):
        for j in xrange(1,t+1):
            if len(str(num))==len(str(num*j)):
                if str(num*j).count(i)==1:
                    count+=1
                
    if count==len(str(num))*t:
        print num
        break
    num+=1

print time.time()-start   
    
#142857 9.22899985313
