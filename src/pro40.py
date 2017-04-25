import time
start=time.time()
n=1000000
st=''
for i in xrange(0,n):
   st+=str(i)
print int(st[1])*int(st[10])*int(st[100])*int(st[1000])*int(st[10000])*int(st[100000])*int(st[1000000])
print time.time()-start
