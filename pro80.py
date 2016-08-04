import decimal
decimal.getcontext().prec=102

def Degital_Sum(number):
    number=str(number)
    digi_sum=0
    for i in number:
        digi_sum+=int(i)
    return digi_sum

digi_sum=0

for i in xrange(1,101):
    num=decimal.Decimal(i).sqrt()
    if num%1:
        num=str(num).split('.')
        num=str(num[0])+str(num[1])
        digi_sum+=Degital_Sum(num[:100])

print digi_sum

#40886
