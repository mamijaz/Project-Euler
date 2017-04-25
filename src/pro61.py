import time
start=time.time()
def Is_Triangle(num):
    if not (((8*num+1)**0.5-1)/2.0)%1:
        return True
    
def Is_Square(num):
    if not (num**0.5)%1:
        return True
    
def Is_Pentogen(num):
    if not (((24*num+1)**0.5+1)/6.0)%1:
        return True
    
def Is_Hexagon(num):
    if not (((8*num+1)**0.5+1)/4)%1:
        return True
    
def Is_Heptagonal(num):
    if not (((40*num+9)**0.5+3)/10)%1:
        return True
    
def Is_Octagonal(num):#fault heare
    if not (((3*num+1.0)**0.5+1.0)/3.0)%1:
        return True

pool=[]
for i in range(1000,10000):
    if Is_Triangle(i)or Is_Square(i) or Is_Pentogen(i) or Is_Hexagon(i) or Is_Heptagonal(i) or Is_Octagonal(i):
        pool.append(i)
pool=list(set(pool))

def Cyclic():
    for i in pool:
        for j in pool:
            if not str(i)[-2:]==str(j)[0:2]:continue
            for k in pool:
                if not str(j)[-2:]==str(k)[0:2]:continue
                for l in pool:
                    if not str(k)[-2:]==str(l)[0:2]:continue
                    for m in pool:
                        if not str(l)[-2:]==str(m)[0:2]:continue
                        for n in pool:
                            if not str(m)[-2:]==str(n)[0:2]:continue
                            if str(n)[-2:]==str(i)[0:2]:
                                pool2=[i,j,k,l,m,n]
                                if len(set(pool2))==6:
                                    tri,sqr,pen,hexa,hepta,octa=0,0,0,0,0,0
                                    for o in pool2:
                                        if Is_Triangle(o):tri+=1
                                        if Is_Square(o):sqr+=1
                                        if Is_Pentogen(o):pen+=1
                                        if Is_Hexagon(o):hexa+=1
                                        if Is_Heptagonal(o):hepta+=1
                                        if Is_Octagonal(o):octa+=1
                                    if tri and sqr and sqr<=tri and pen and pen<=sqr and hexa and hexa<=pen and hepta and hepta<=hexa and octa and octa<=hepta:
                                        return pool2

pool2=Cyclic()                                        
print pool2
print sum(pool2)
print time.time()-start
#28684 4.52999997139
