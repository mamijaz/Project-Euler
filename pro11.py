fo=open('input_pro11.txt','r+')
s=(fo.read()).split()
for i in range(len(s)):s[i]=int(s[i])

multp=1
s1=[]
n=4

for i in range(20):
    s2=[]
    for j in range(20):
        s2.append(s[0])
        s.remove(s[0])
    s1.append(s2)

for i in range(20):
    for j in range(16):
        multp1=1
        for k in range(n):
            multp1=multp1*s1[i][j+k]
        if multp1>multp:multp=multp1


for i in range(20-n):
    for j in range(20):
        multp1=1
        for k in range(n):
            multp1=multp1*s1[i+k][j]
        if multp1>multp:multp=multp1

for i in range(20-n):
    for j in range(20-n):
        multp1=1
        for k in range(n):
            multp1=multp1*s1[i+k][j+k]
        if multp1>multp:multp=multp1
        
for i in range(20-n):
    for j in range(n-1,20):
        multp1=1
        for k in range(n):
            multp1=multp1*s1[i+k][j-k]
        if multp1>multp:multp=multp1
            
print multp
        
    
        
        
fo.close()
