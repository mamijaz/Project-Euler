from fractions import Fraction

number=1
for i in range(11,100):
    for j in range(11,100):
        num=Fraction(i,j)
        if num<1 and int(str(i)[1]) and int(str(j)[1]):
            if int(str(i)[0])==int(str(j)[0]):
                if num==Fraction(int(str(i)[1]),int(str(j)[1])):
                    number*=num
            elif int(str(i)[0])==int(str(j)[1]):
                if num==Fraction(int(str(i)[1]),int(str(j)[0])):
                    number*=num
            elif int(str(i)[1])==int(str(j)[0]):
                if num==Fraction(int(str(i)[0]),int(str(j)[1])):
                    number*=num
            elif int(str(i)[1])==int(str(j)[1]):
                if num==Fraction(int(str(i)[0]),int(str(j)[0])):
                    number*=num
print number
#100
