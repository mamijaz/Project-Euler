def get_input_matrix(name,order):
    fo=open(name,'r+')
    string=(fo.read()).split('\n')
    fo.close()
    metrix=[]
    for line in string[0:order]:
        met=line.split(',')
        for i in range(len(met)):
            met[i]=int(met[i])
        metrix.append(met[::-1])
    return metrix

order=80
metrix=get_input_matrix('tttt.txt',order)
msum=[]
for i in range(order):
    minsum=0
    col=0
    row=i
    while True:
        if col==order-1:
            minsum+=(metrix[row][col])
            break
        elif row==0:
            b=metrix[row][col+1]
            c=metrix[row+1][col]+metrix[row+1][col+1]
            if b<c:
                minsum+=(metrix[row][col])
            elif c<b:
                minsum+=(metrix[row][col]+metrix[row+1][col])
                row+=1
            else:
                print 'error'
        elif row==order-1:
            a=metrix[row-1][col]+metrix[row-1][col+1]
            b=metrix[row][col+1]
            if a<b:
                minsum+=a
                row-=1
            elif b<a:
                minsum+=(metrix[row][col])
            else:
                print 'error'
        else:
            a=metrix[row-1][col]+metrix[row-1][col+1]
            b=metrix[row][col+1]
            c=metrix[row+1][col]+metrix[row+1][col+1]
            if a<min(b,c):
                minsum+=(metrix[row][col]+metrix[row-1][col])
                row-=1
            elif b<min(a,c):
                minsum+=(metrix[row][col])
            elif c<min(a,b):
                minsum+=(metrix[row][col]+metrix[row+1][col])
                row+=1
            else:
                print 'error'
        col+=1
    msum.append(minsum)
            

print min(msum)
print msum

