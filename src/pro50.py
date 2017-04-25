def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True
    
lim=1000000
prime=[]
i=2
num=0
while True:
    if IsPrime(i):
        num+=i
        prime.append(i)
    if num>lim:break
    i+=1

length=0
pri=0
         
for i in xrange(0,len(prime)):
    for j in xrange(-len(prime),i):
        if len(prime[i:j])>length:
            if IsPrime(sum(prime[i:j])) and sum(prime[i:j])<lim :
                length=len(prime[i:j])
                pri=sum(prime[i:j])
                
print pri,length
#997651 543
