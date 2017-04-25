import time

def Square_Digit_Chain(num):
    sq_sum=0
    for i in str(num):
        sq_sum+=int(i)**2
    return sq_sum

start=time.time()

count=0
num_range=10000000

print num_range

for i in xrange(1,num_range):
    num=i
    while True:
        if num==89:
            count+=1
            break
        elif num==1:
            break
        else:
            num=Square_Digit_Chain(num)
        
print count
print time.time()-start

#8581146
#497.99000001
