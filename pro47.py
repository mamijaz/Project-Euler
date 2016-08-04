import time

start=time.time()

def Prime_Factors(num):
    pf_list1=[]
    pf_list2=[]
    pf=2
    while not num%2:
        num=num/pf
        pf_list1.append(pf)

    pf=3   
    while num!=1:
        while not (num%pf):
            num=num/pf
            pf_list1.append(pf)
        pf+=2
    for i in set(pf_list1):
        pf_list2.append(i**pf_list1.count(i))
        
    return pf_list2

dpf=4
num=1
while True:
    count=dpf
    for i in xrange(dpf):
        if len(Prime_Factors(num+i))!=dpf:
            count-=1
            break
    if count==dpf:
        nums=[]
        for i in range(dpf):
            for j in Prime_Factors(num+i):
                nums.append(j)
        if len(set(nums))==dpf**2:   
            print num
            break
    num+=1
print time.time()-start
# 134043  194.792999983 
