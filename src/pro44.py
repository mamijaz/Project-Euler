import itertools
import time

start=time.time()

def Is_Pentogen(num):
    if not (((2.0*num)/3+1.0/36)**0.5+1.0/6)%1:
        return True  

a=[]
for i in range(1,5000):
    a.append(i*(3*i-1)/2)
    
b=list(itertools.combinations(a,2))

for i in b:
    if Is_Pentogen(i[0]+i[1]) and Is_Pentogen(i[1]-i[0]):
        print i
        print i[1]-i[0]
print time.time()-start

#5482660
