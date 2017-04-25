import time

start=time.time()

f_n_1=1
f_n_2=1
f_count=2

while True:
    f_n=f_n_1+f_n_2
    f_count+=1
    if not f_count%10000:
        print f_count
    count=1
    for i in '123456789':
        if i not in str(f_n)[0:9] or i not in str(f_n)[::-1][0:9]:
            count=0
            break
    if count:
        print f_n,f_count
        break
    f_n_1,f_n_2=f_n,f_n_1

print time.time()-start    
