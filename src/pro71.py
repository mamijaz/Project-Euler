import time

d=1000000
frac=[]
numarator=[]

start=time.time()

for den in range(int(d/2),int(d+1)):
    for neu in range(int(den/4),int(d/2)):
        if  float(3)/7>float(neu)/den:
            frac.append(float(neu)/den)
            numarator.append(neu)

index=frac.index(max(frac))
print (numarator[index])
print (time.time()-start)



