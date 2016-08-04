for x in range(16,25):
    for y in range(1,16):
        a=x**2-y**2
        b=2*x*y
        c=x**2+y**2
        if a+b+c==1000:
            print a*b*c
            break
#31875000
