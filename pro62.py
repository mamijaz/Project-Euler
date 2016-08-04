import itertools
import time

def Cubic_Permutations(counts):
    length=1
    while True:
        cubes=[]
        minimum=int(round(int('1'+'0'*(length-1))**(1.0/3)))
        maximum=int(round(int('1'+'0'*(length))**(1.0/3)))
        for i in range(minimum,maximum):
            num=str(i**3)
            if len(num)==length:
                cubes.append(num)
        for i in range(len(cubes)):
            count=[]
            for j in range(len(cubes)):
                count2=1
                for k in cubes[i]:
                    if cubes[i].count(k)!=cubes[j].count(k):
                        count2=0
                if count2:
                    count.append([int(round(int(cubes[j])**(1.0/3))),cubes[j]])
            if len(count)==counts:
                return count
        length+=1

start=time.time()
print Cubic_Permutations(5)
print time.time()-start

#127035954683
#125.747999907
