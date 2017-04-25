import time
start=time.time()
list1=[]
a=100
b=100
for i in range(2,a+1):
    for j in range(2,b+1):
        if not list1.count(i**j):list1.append(i**j)
print len(list1)
print time.time()-start
