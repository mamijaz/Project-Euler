import time

start=time.time()
n=1000000
double_base_palindrome=[]

for i in range(1,n):
    if str(i)==str(i)[::-1]:
        a=str(bin(i))[2:]
        if a==a[::-1]:
            if a[::-1][0]!=0:
                double_base_palindrome.append(i)

print double_base_palindrome
print sum(double_base_palindrome)

print time.time()-start  
