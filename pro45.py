import time

start=time.time()

def Is_Pentogen(num):
    if not (((2.0*num)/3+1.0/36)**0.5+1.0/6)%1:
        return True
    
def Is_Hexagon(num):
    if not ((num/2.0+1.0/16)**0.5+1.0/4)%1:
        return True
    
t=[]
for i in range(1,100000):
    t.append(i*(i+1)/2)

for i in t:
    if Is_Hexagon(i):
        if Is_Pentogen(i):
            print i
            
print time.time()-start

#1533776805
