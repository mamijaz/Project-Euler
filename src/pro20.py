def Factorial_Digit_Sum(num):
    fac=1
    tot=0
    for i in range(1,num+1):
        fac*=i
    for i in str(fac):
        tot+=int(i)
    return tot

print Factorial_Digit_Sum(100)
