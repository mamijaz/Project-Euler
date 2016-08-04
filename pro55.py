def Is_Lychrel(num,count=0):
    if num==int(str(num)[::-1])and count>0:
        return False
    elif count<50:
        count+=1
        return Is_Lychrel(num+int(str(num)[::-1]),count)
    else:
        return True

count=0
for i in xrange(1,10000):
    if Is_Lychrel(i):
        count+=1
        
print count

#249
