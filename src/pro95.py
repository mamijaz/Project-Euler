import time

def Proper_Divisors_Sum(num):
    Proper_D=[1]
    for i in xrange(2,int(num**0.5)+1):
        if not num%i:
            if i not in Proper_D:Proper_D.append(i)
            if num/i not in Proper_D:Proper_D.append(num/i)
    return sum(Proper_D)

def Amicable_Chain_Length(num):
    ami_num=[num]
    while True:
        if num>1000000: 
            return 0
        if ami_num.count(num)>1:
            if num!=ami_num[0]:
                return 0
            else:
                return len(ami_num)-1
        num=Proper_Divisors_Sum(num)
        ami_num.append(num)
    

start=time.time()

max_length=0
number=0
num_range=1000000

print num_range

for num in xrange(1,num_range):
    length=Amicable_Chain_Length(num)
    if length>max_length:
        max_length=length
        number=num

print number,max_length
print time.time()-start

#14316 28       
#452.779999971  
