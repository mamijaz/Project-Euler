fo=open('input_pro67.txt','r')
st=(fo.read()).split('\n')
for i in xrange(len(st)):
    st[i]=st[i].split()
    for j in xrange(len(st[i])):
        st[i][j]=int(st[i][j])

for  i in xrange(len(st)-2,-1,-1):
    for j in xrange(len(st[i])):
        st[i][j]+=max(st[i+1][j],st[i+1][j+1])
print st[0][0]

#7273
