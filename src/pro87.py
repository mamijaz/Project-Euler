def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True

def Pro_Prime(limit):
    primes=[]
    if limit>=3:
        prime2.append(2**2)
        prime3.append(2**3)
        prime4.append(2**4)
    for num in range(3,limit,2):
        if IsPrime(num):
            prime2.append(num**2)
            prime3.append(num**3)
            prime4.append(num**4)

prime_range=7200
target=50000000

prime2=[]
prime3=[]
prime4=[]
Pro_Prime(prime_range)
nums=[]

for i in prime2:
    for j in prime3:
        for k in prime4:
            if i+j+k<target:
                nums.append(i+j+k)
            else:
                break
                
print target,prime_range,len(set(nums))
#1097343
