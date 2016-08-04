import time

def Factorial(num):
    if num==1 or num==0:
        return 1
    else:
        return num*Factorial(num-1)

def Digit_Factorial(num):
    num=str(num)
    factorial=0
    for i in num:
        factorial+=Factorial(int(i))
    return factorial

def Count_Digit_Factorial(num):
    digi_facs=[num]
    count=1
    while count<=60:
        num=Digit_Factorial(num)
        if num not in digi_facs:
            digi_facs.append(num)
            count+=1
        else:
            return count

start=time.time()
    
num_Range=1000000
count=0
for num in xrange(1,num_Range):
    if Count_Digit_Factorial(num)==60:
        count+=1


print count
print time.time()-start

#402
#477.66
