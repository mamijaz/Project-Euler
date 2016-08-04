def Factorial(num):
    if num==0:
        return 1
    else:
        return num*Factorial(num-1)

def nCr(n,r):
    return Factorial(n)/(Factorial(r)*Factorial(n-r))

count=0
for n in xrange(1,100+1):
    for r in xrange(0,n+1):
        if nCr(n,r)>1000000:
            count+=1

print count

#4075
