import itertools
import time

start=time.time()

n=28124
abundent_numbers=[]
numbers=(n-1)*(n)*0.5
numbers2=[]

def Proper_Divisors(num):
    Proper_D=[1]
    for i in xrange(2,int(num**0.5)+1):
        if not num%i:
            if i not in Proper_D:Proper_D.append(i)
            if num/i not in Proper_D:Proper_D.append(num/i)
    return sum(Proper_D)

for i in xrange(1,n):
    if i<Proper_Divisors(i):abundent_numbers.append(i)

a=list(itertools.combinations_with_replacement(abundent_numbers, 2))

for i in xrange(len(a)):
    b=int(a[i][0])+int(a[i][1])
    if b<28124:
            numbers2.append(b)
                 
print int(numbers-sum(list(set(numbers2))))

print time.time()-start        

