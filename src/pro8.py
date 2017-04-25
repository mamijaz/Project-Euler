fo=open('input_pro8.txt','r+')
s1=(fo.read()).split()
s2=''
n=13
multp1=1
for i in s1:
    s2=s2+i
for i in range(len(s2)-n):
    multp2=1
    for j in range(n):
        multp2=multp2*int(s2[i+j])
    if multp2>multp1:multp1=multp2
        
print multp1
fo.close()
