import decimal
decimal.getcontext().prec =100
print decimal.Decimal(1)/decimal.Decimal(7)
for d in range(1,1000):
    dec=decimal.Decimal(1)/decimal.Decimal(d)
    print dec,d
