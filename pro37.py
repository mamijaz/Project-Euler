import time

start=time.time()

trunk_prime_count=[]

def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num!=1:
        return True
    
t_p_c=0
i=10
while t_p_c<11:
    if IsPrime(i):
        a=[]
        st=str(i)
        for j in range(len(str(i))):
            a.append(int(st[j:]))
            a.append(int(st[0:j+1]))
        count=1
        for j in a:
            if not IsPrime(j):
                count=0
                break
        if count==1:
            trunk_prime_count.append(i)
            t_p_c+=1
    i+=1

print trunk_prime_count
print sum(trunk_prime_count)
print time.time()-start
        
