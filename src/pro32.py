import time

start=time.time()

def Pen_Product(num):
    for i in xrange(2,int(num**0.5)+1):
        if not num%i:
            count=0
            for j in range(1,10):
                a=str(i)+str(num/i)+str(num)
                if len(a)==9:
                    if a.count(str(j))==1:
                        count+=1
                    else:break
                else:break
            if count==9:
                return True

pen_product_numbers=[]

for i in range(1,10000):
    if Pen_Product(i):
        pen_product_numbers.append(i)

print pen_product_numbers
print sum(pen_product_numbers)
print time.time()-start
