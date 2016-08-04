
def IsPrime(num):
    j=2
    while j**2<=num:
        if not num%j:break
        j=j+1
    if j**2>num and num>1:
        return True
    
for i in xrange(1000,3333):
    if IsPrime(i):
        if IsPrime(i+3330):
            if IsPrime(i+3330*2):
                count=0
                for j in str(i):
                    if j in str(i+3330) and j in str(i+3330*2):
                        count+=1
                if count==4:print str(i)+str(i+3330)+str(i+3330*2)

#296962999629
