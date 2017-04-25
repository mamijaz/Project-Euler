import time
d=12000
frac=[]

start=time.time()

for den in range(1,d+1):
    for neu in range(1,den):
        if float(neu)/den>float(1)/3 and float(1)/2>float(neu)/den:
            frac.append(float(neu)/den)

frac=list(set(frac))
print len(frac)
print time.time()-start

#7295372
#109.878999949
