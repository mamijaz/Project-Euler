def Singuler_Intiger_Right_Triangle(length):
    count_X=[]
    if length%2:
        return 0
    for x in range(1,length):
        for y in range(1,length):
            a=x**2-y**2
            b=2*x*y
            c=x**2+y**2
            if a+b+c==length and a>0 and b>0 and c>0:
                count_X.append([a,b,c])
    return count_X
    
print Singuler_Intiger_Right_Triangle(1500000)
