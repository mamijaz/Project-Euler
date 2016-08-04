import itertools
import time

start=time.time()

sum=0
a=list(itertools.permutations(range(10), 10))
for i in a:
    if i[0]!=0:
        if not int(str(i[1])+str(i[2])+str(i[3]))%2:
            if not int(str(i[2])+str(i[3])+str(i[4]))%3:
                if not int(str(i[3])+str(i[4])+str(i[5]))%5:
                    if not int(str(i[4])+str(i[5])+str(i[6]))%7:
                        if not int(str(i[5])+str(i[6])+str(i[7]))%11:
                            if not int(str(i[6])+str(i[7])+str(i[8]))%13:
                                if not int(str(i[7])+str(i[8])+str(i[9]))%17:
                                    b=''
                                    for j in i:
                                        b+=str(j)
                                    sum+=int(b)
                                    print b
print sum

print time.time()-start
#16695334890
