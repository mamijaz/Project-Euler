r=10000
amicable_numbers=[]

def Proper_Divisors_Sum(num):
    Proper_D=[1]
    for i in xrange(2,int(num**0.5)+1):
        if not num%i:
            if i not in Proper_D:Proper_D.append(i)
            if num/i not in Proper_D:Proper_D.append(num/i)
    return sum(Proper_D)

def Amicable_Pairs(num):
    num1=Proper_Divisors_Sum(num)
    num2=Proper_Divisors_Sum(num1)
    if num==num2 and num!=num1:
        amicable_numbers.append(num)
        amicable_numbers.append(num1)

for i in xrange(1,r):
    if i not in amicable_numbers:
       Amicable_Pairs(i)

print sum(amicable_numbers)


